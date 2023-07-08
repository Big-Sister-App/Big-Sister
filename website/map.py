import os
import googlemaps
import pandas as pd
import sqlite3


# DATABASE CONNECTIONS & SETUP
#--------------------------------------------------------
# Our Database of Reports
conn2 = sqlite3.connect("databases/reports.db")
cursor2 = conn2.cursor()

createTable = """CREATE TABLE IF NOT EXISTS
reports(id INTEGER PRIMARY KEY autoincrement, date TEXT, typeOfReport TEXT, reportDesc TEXT, location TEXT)"""
cursor2.execute(createTable)

# cursor2.execute(
#      "INSERT INTO {tableName} (date, typeOfReport, reportDesc, location) VALUES(?, ?, ?, ?)".format(tableName="reports"), 
#      (datetime.now(), "Harassment", "Some explanation can go here ig", "346 Huntington Avenue"))
#  conn2.commit()

# CONVERT DB FILE TO CSV
#--------------------------------------------------------
reports = pd.read_sql("SELECT * FROM reports", conn2)
reports.to_csv("reports.csv", index=False)

reports_table = pd.read_csv("reports.csv", encoding="ISO-8859-1")
df = reports_table.copy()
#print(df.head())


# GEOCODING
#--------------
gmaps_key = googlemaps.Client(key=os.environ['GMAPS_API_KEY'])

# Convert address into longitude and latitude format
def geocode_address(address):
    a = gmaps_key.geocode(address)
    lat = a[0]["geometry"]["location"]["lat"]
    long = a[0]["geometry"]["location"]["lng"]
    return(lat, long)
    # print(f'Latitude: {str(lat)}, Longitude: {str(long)}')

# apply geocoding function to physical location
df['gc_address'] = df['location'].apply(geocode_address)
print(df.head)

marker_locations = df['gc_address'].values.tolist() #list of all lat, lng pairs
import os
from flask import Blueprint, render_template, request, redirect, url_for, send_file
import sqlite3
from website.map import LocationCuration
from dotenv import load_dotenv

load_dotenv()

views = Blueprint('views', __name__) 
geocoder = LocationCuration(os.getenv('GMAPS_API_KEY'))

#SQLITE FOR RECEIVING EMAILS DATABASE
conn2  = sqlite3.connect("databases/recieve_emails.db")
cursor2 = conn2.cursor()

createTable = """CREATE TABLE IF NOT EXISTS
emailR(id INTEGER PRIMARY KEY autoincrement, emails TEXT)"""
cursor2.execute(createTable)


# HOME PAGE
#---------------------------------------------
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html", map_link=os.getenv('MAP_API_LINK'))


# ABOUT PAGE
#---------------------------------------------
@views.route('/about')
def about_us():
    return render_template("about.html") 


# RESOURCES PAGE
#---------------------------------------------
@views.route('/mentalhealth', methods=['GET', 'POST'])
def resources():
    return render_template("mentalhealth.html")    


# GET JSON
#---------------------------------------------
@views.route('/databases/geocoded_data.json')
def get_json():
    return send_file('../databases/geocoded_data.json')


# REPORT PAGE 
#---------------------------------------------
@views.route('/report', methods=['GET', 'POST'])
def make_report():
    if request.method == 'POST':
        t_report = request.form.get('t_report_field')
        r_desc = request.form.get('r_desc_field')
        l_loc = request.form.get('l_loc_field')

        # report = {
        #     "typeOfReport": t_report,
        #     "reportDesc": r_desc,
        #     "location": l_loc
        # } 
        # geocoder.add_to_table(report_info=report)
        # geocoder.geocode_and_export()
        return redirect(url_for("map.html"))
    
    return render_template("report.html")

        

# # EMAILS PAGE
# #---------------------------------------------
# # Checks if emails already is in the database
# # if it does then tell user else inserts to the table
# def duplicate(email_address):
#     cursor2.execute("""SELECT * FROM emailR""")
#     result = cursor2.fetchall
#     if result == "emails":
#         print("EMAIL EXISTS")
#     else:
#         cursor.execute("INSERT INTO {tableName} (emails) VALUES(?)".format(tableName="emailR"), (email_address))
#     conn.execute()

# # Inserts emails from webpage into table
# @views.route('/receive-alerts', methods=['GET', 'POST'])
# def receive_emails():
#     if request.method == 'POST':
#         email_address = request.form.get('email_field')
#         duplicate(email_address)
#         cursor2.execute("INSERT INTO {tableName} (emails) VALUES(?)".format(tableName="emailR"), (email_address))
#         conn2.commit()       
#     return render_template("emails.html")



        
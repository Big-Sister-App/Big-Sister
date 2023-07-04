#this file will store the different pages users can go topop
from flask import Blueprint, jsonify, render_template, flash, request, jsonify
import json
import sqlite3
import  requests


views = Blueprint('views', __name__) #dont need to name it after the file, its just easier
# @<name_of_the_view>.route('/<url to get to the page')


# SQLITE CONNECTIONS & TABLE CREATION
#---------------------------------------------
#SQLITE FOR RECEIVING EMAILS DATABASE
conn  = sqlite3.connect("recieve_emails.db")
cursor = conn.cursor()

createTable = """CREATE TABLE IF NOT EXISTS
emailR(id INTEGER PRIMARY KEY autoincrement, emails TEXT)"""
cursor.execute(createTable)

#SQLITE FOR REPORT DATABASE
conn2 = sqlite3.connect("reports.db")
cursor2 = conn2.cursor()

createTable = """CREATE TABLE IF NOT EXISTS
reports(id INTEGER PRIMARY KEY autoincrement, date TEXT, typeOfReport TEXT, reportDesc TEXT, location TEXT)"""
cursor2.execute(createTable)


# HOME PAGE
#---------------------------------------------
@views.route('/', methods=['GET', 'POST'])
def home():
    "Home page shit here"
    return render_template("HomePage.html")    


# ABOUT PAGE
#---------------------------------------------
@views.route('/about')
def about_us():
    "About page shit here"
    return render_template("About.html") 


# EMERGENCY PAGE
#---------------------------------------------
@views.route('/emergency')
def emergency():
    "Emergency page shit here"
    return render_template("Emergency.html") 


# REPORT PAGE 
#---------------------------------------------
# Filters reports
def filter(t_report):
    cursor.execute("""SELECT typeOfReport FROM reports WHERE typeofReport NOT LIKE 'Fuck%'; """)
    t_report = cursor.fetchall
    if t_report == "typeOfReport":
        cursor.execute("INSERT INTO {tableName} (typeOfReport) VALUES(?)".format(tableName="reports"), (t_report))
    else: 
        print ("Innapropiate Language")
        conn.execute()

@views.route('/report', methods=['GET', 'POST'])
def make_report():
    "Report stuff here"
    if request.method == 'POST':
        t_report = request.form.get('t_report_field')
        filter(t_report)
        r_desc = request.form.get('r_desc_field')
        l_loc = request.form.get('l_loc_field')
        cursor2.execute("INSERT INTO {tableName} (typeOfReport, reportDesc, location) VALUES(?, ?, ?)".format(tableName="reports"),(t_report, r_desc, l_loc))
    return render_template("Report.html")

        

# EMAILS PAGE
#---------------------------------------------
# Checks if emails already is in the database
# if it does then tell user else inserts to the table
def duplicate(email_address):
    cursor.execute("""SELECT * FROM emailR""")
    result = cursor.fetchall
    if result == "emails":
        print("EMAIL EXISTS")
    else:
        cursor.execute("INSERT INTO {tableName} (emails) VALUES(?)".format(tableName="emailR"), (email_address))
    conn.execute()

# Inserts emails from webpage into table
@views.route('/receive-alerts', methods=['GET', 'POST'])
def receive_emails():
    if request.method == 'POST':
        email_address = request.form.get('email_field')
        duplicate(email_address)
        cursor.execute("INSERT INTO {tableName} (emails) VALUES(?)".format(tableName="emailR"), (email_address))
        conn.commit()       
    return render_template("emails.html")



        
# Just click run and the email will send automatically :)

# Credits: The PyCoach

# Note: Gmail API was not used like before with client json files or other stuff present before
#       This format is strictly for sending emails from the given sender to the given user(s)

from email.message import EmailMessage
import ssl
import smtplib

# This is the random email account I (Paula) made (let me know if you need the password at any time)
big_sister_email = 'bigsistermain@gmail.com'

# Using 2 step authentication I got this 12 character password that will allow an automatic sign-in to this email
big_sister_password = 'wginrogrclwlabwj'

# The numbers in bcc should be replaced with people's emails and for each element in the list it'll send the email to the element
cc = ['bigsistermain@gmail.com']
bcc = ['__(1)__@___.__', '__(2)__@___.__', '__(3)__@___.__', '__(4)__@___.__', '__(5)__@___.__']

# Change the subject of the email if need be
subject = 'BIG SISTER ALERT!'

# Body of the email that will be based on the alert itself
body = """
************************* ALERT *************************


When alerts are made, they will be pasted here


************************* ALERT *************************
Big Sister
You'll Never Walk Alone
"""

context = ssl.create_default_context()

# Credit to Leonardo Andrade in stackoverflow for how to implement my bcc idea
message = "From: %s\r\n" % big_sister_email + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % subject + "\r\n" + body
recipients = cc + bcc
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
# Login using aforementioned BigSister email and password
server.login(big_sister_email, big_sister_password)
server.set_debuglevel(1)
# Send the alert from BigSister to the users as an email
server.sendmail(big_sister_email, recipients, message)
server.quit()

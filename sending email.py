import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'From Email'
EMAIL_PASS = 'Your email password'
EMAIL_RECIEVER = 'Reciever Email'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

   smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

   msg = EmailMessage()
   msg['Subject'] = 'This is the subject'
   msg['From'] = EMAIL_ADDRESS
   msg['To'] = EMAIL_RECIEVER

   msg.set_content('This is the email content')

   msg.add_alternative("""\
   <!DOCTYPE html>
   <html>
       <body>
           <h1 style="color:SlateGray;">Have a good day :)</h1>
       </body>
   </html>
   """, subtype='html')

   smtp.send_message(msg)

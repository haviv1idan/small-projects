import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'Haviv1idan@gmail.com'
EMAIL_PASS = 'haviv5696'
EMAIL_RECIEVER = 'Haviv1idan@gmail.com'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

   smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

   msg = EmailMessage()
   msg['Subject'] = 'This is Idan Haviv spam'
   msg['From'] = EMAIL_ADDRESS
   msg['To'] = EMAIL_RECIEVER

   msg.set_content('This is Idan mail')

   msg.add_alternative("""\
   <!DOCTYPE html>
   <html>
       <body>
           <h1 style="color:SlateGray;">Have a good day :)</h1>
       </body>
   </html>
   """, subtype='html')

   smtp.send_message(msg)

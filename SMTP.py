import os
from email.message import EmailMessage 
from datetime import datetime
import ssl
import smtplib
from dotenv import load_dotenv
load_dotenv()

current_datetime = datetime.now()
email_sender = os.environ.get('MAIL_USERNAME')
email_password = os.environ.get('MAIL_PASSWORD')
email_receiver = os.environ.get('MAIL_USERNAME')

subject = 'Scraping is done! Check Out for more details'
body = f"""Web Scraping is done. Open Visual Studio for more details {current_datetime} """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
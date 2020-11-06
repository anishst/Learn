import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

with open('gmail_credentials.json') as json_data_file:
    data = json.load(json_data_file)
email = data['email']
pwd = data['password']


server = smtplib.SMTP( "smtp.gmail.com", 587 ) # add these 2 to .yml as well
server.starttls()
server.login(email, pwd)

msg = MIMEMultipart()
msg['Subject'] = 'Testing Attachment'
msg['From'] = '<email_id>'
recipients = ['<email_id>']
msg['To'] = ", ".join(recipients)
body = "<b>See Attachment</b>"
msg.attach(MIMEText(body, 'html'))

file = 'la_trip_2019_ticket_prices.csv'
with open(file, 'r') as fp:
	img = MIMEText(fp.read())
msg.attach(img)

server.send_message(msg)
server.quit()

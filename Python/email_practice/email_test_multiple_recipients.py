import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


GMAIL_USER =  "<email_id>"
GMAIL_PASS = "<app pwd>" # created using app password in gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


msg = MIMEMultipart()
msg['Subject'] = 'Testing Attachment'
msg['From'] = '<email_id>'
recipients = ['<email_id>','<email id>']
msg['To'] = ", ".join(recipients)
body = "<b>See Attachment</b>"
msg.attach(MIMEText(body, 'html'))

file = 'image.png'
with open(file, 'rb') as fp:
	img = MIMEImage(fp.read())
msg.attach(img)

csv_file = 'sample_csv.csv'
with open(csv_file, 'r') as fp:
	text_file = MIMEText(fp.read())
msg.attach(text_file)

smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpserver.starttls()
smtpserver.login(GMAIL_USER, GMAIL_PASS)
smtpserver.send_message(msg)
smtpserver.quit()

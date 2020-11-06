import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


GMAIL_USER =  "<email_id>"
GMAIL_PASS = "<apppwd>" # created using app password in gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

msg = MIMEMultipart()
msg['Subject'] = 'Testing Attachment'
msg['From'] = '<email_id>'
msg['To'] = '<email_id>'
body = "<b>See Attachment</b><font color='red'>test</font>"
msg.attach(MIMEText(body, 'html'))

file = 'IMAGE.png'
with open(file, 'rb') as fp:
	img = MIMEImage(fp.read())
msg.attach(img)

smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpserver.starttls()
smtpserver.login(GMAIL_USER, GMAIL_PASS)
smtpserver.send_message(msg)
smtpserver.quit()

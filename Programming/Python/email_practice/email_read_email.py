# http://www.vineetdhanawat.com/blog/2012/06/how-to-extract-email-gmail-contents-as-text-using-imaplib-via-imap-in-python-3/
import smtplib
import imaplib
import email


GMAIL_USER =  "<email_id>"
GMAIL_PASS = "Pa$$word1" # created using app password in gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


	
try:
	mail = imaplib.IMAP4_SSL(SMTP_SERVER)
	mail.login(GMAIL_USER, GMAIL_PASS)
	# print(mail.list())
	print("Logged in")
	mail.select('inbox')
	result, data = mail.uid('search', None, '(HEADER Subject "Account new password information")')
	print(result, data[0])
		# search and return uids instead
	i = len(data[0].split()) # data[0] is a space separate string
	print(f"Found {i} messsages ")
	for x in range(1):
		latest_email_uid = data[0].split()[x] # unique ids wrt label selected
		result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
		# fetch the email body (RFC822) for the given ID
		raw_email = email_data[0][1]
		print(raw_email)

		#continue inside the same for loop as above
		raw_email_string = raw_email.decode('utf-8')
		# converts byte literal to string removing b''
		email_message = email.message_from_string(raw_email_string)
		# this will loop through all the available multiparts in mail
		for part in email_message.walk():
		 if part.get_content_type() == "text/plain": # ignore attachments/html
		  body = part.get_payload(decode=True)
		  save_string = str("Dumpgmailemail_" + str(x) + ".txt")
		  print(body.decode('utf-8'))
		  # location on disk
		  myfile = open(save_string, 'a')
		  myfile.write(body.decode('utf-8'))
		  # body is again a byte literal
		  myfile.close()
		 else:
		  continue



except Exception as e:
	raise e


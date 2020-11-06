"""
This script will read email from gmail folder
"""
import imaplib
import email
import re

# user credentials
gmail_username =  "<email_id>"
gmail_password = "Pa$$word1" 

#  login to IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(gmail_username, gmail_password)

# select inbox
mail.select('inbox')

# read binary info about messages
# for ALL items
# result, data = mail.uid('search', None, 'ALL')

# for certain subject items
result, data = mail.uid('search', None, '(HEADER Subject "Account new password information")')

# convert to a list
inbox_item_list  = data[0].split()

# find most recent item
most_recent = inbox_item_list[-1]
print(inbox_item_list[-1])
result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')
raw_email = email_data[0][1].decode('utf-8')

pwdregex = r"Password:.+" # get temp pwd
matches = re.findall(pwdregex, raw_email)
pwdstring = matches[0]
pwdstring = pwdstring.replace('\\n','')
pwdstring = pwdstring.replace('Password: ','')
print(pwdstring)



# https://www.youtube.com/watch?v=kWyoYtvJpe4
#https://docs.python.org/2/howto/regex.html
#https://regexone.com/references/python
# https://developers.google.com/edu/python/regular-expressions
# https://pythex.org/ # practice tool
import re

# regex = r"(Temporary Password: [vI%49*J\r)"
# tempPwd = """[27194]
# 1 messages that aren't deleted
# defaultdict(<class 'dict'>, {27194: {b'BODY[]': b'Delivered-To: automatedotcnetuser+1212@gmail.com\r\nReceived: by 10.100.137.16 with SMTP id n16csp875209pjn;\r\n        Thu, 25 May 2017 11:19:46 -0700 (PDT)\r\nX-Received: by 10.237.55.193 with SMTP id j59mr1271764qtb.238.1495736386221;\r\n        Thu, 25 May 2017 11:19:46 -0700 (PDT)\r\nARC-Seal: i=1; a=rsa-sha256; t=1495736386; cv=none;\r\n        d=google.com; s=arc-20160816;\r\n        b=axS4NabTTQA9XrnAJsY79Jjd2vELsjHTImCkvLPAKkYaf2uhsT17Nr0hy0AMNYnK3T\r\n         BTEIypr2xwEhjCkfXM3m7gGfbCykNnmFM0rTZsQn6e+TpZ9+Fj1ozob4TKGddWMpcQIe\r\n         k9IjIFYPM/nWy4+N8LM/uN7X2NJgjVp+ncZ0NgGiQE7+ZQRRLYLvruIxjcav7wJqacHH\r\n         EvM+PT+JgK4xe7qaTpeHWdwd4Y/KcnoIO+fa6dDxzW7lBZ5RW2VXMA47tiV4Icckc/J+\r\n         SC08G9Z1I6jU4g00Jeq6G99OTS9ReOIeMWOhbxXPy24bGW8v53tOyEjfyosC+Wfuq6kJ\r\n         Fjtw==\r\nARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\r\n        h=mime-version:subject:message-id:to:from:date\r\n         :arc-authentication-results;\r\n        bh=gkyMrhD4WJHexZ1ZP+CnCkHvUAw9YTP8zkLbrz3kK4g=;\r\n        b=wrDxPYJRGrV1DTpGyNg4cupEqpJBGE8CkuYaGn6HVSaTV1ePYgqAUJwmDxxY+JRL+w\r\n         6+iX4Feim7/FCBSocPwAyww1NXBpymiEmKJ/NVhluCqdkdh60Xot8vI1aimsFxz4GNEk\r\n         SFO0UZFVb5zPq99LmsDg8HilzcxK8133FQ8in0IBC6H3FqVlcPr+sOR3NCjnV9AxScIO\r\n         vu3dXiy/eTW7VA0RW4UPMVhK1XHaROkNuc2CjsYlqRAkHwbKemWeO6VV1RswWH/8OP3Y\r\n         pUzvnYG8KUjjqe3BzxgvrCKBr+pYfE7OjHK9ZgKLQ3cDufKtp4YljFFhn8le9JHqF/GU\r\n         pKIw==\r\nARC-Authentication-Results: i=1; mx.google.com;\r\n       spf=pass (google.com: domain of donotreply@fms.treas.gov designates 2610:108:4000:100c::215 as permitted sender) smtp.mailfrom=donotreply@fms.treas.gov\r\nReturn-Path: <donotreply@fms.treas.gov>\r\nReceived: from TS-C-X1070-IP1.treasury.gov (pkmailhub1.treasury.gov. [2610:108:4000:100c::215])\r\n        by mx.google.com with ESMTPS id f41si3793397qte.254.2017.05.25.11.19.45\r\n        for <automatedotcnetuser+1212@gmail.com>\r\n        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);\r\n        Thu, 25 May 2017 11:19:46 -0700 (PDT)\r\nReceived-SPF: pass (google.com: domain of donotreply@fms.treas.gov designates 2610:108:4000:100c::215 as permitted sender) client-ip=2610:108:4000:100c::215;\r\nAuthentication-Results: mx.google.com;\r\n       spf=pass (google.com: domain of donotreply@fms.treas.gov designates 2610:108:4000:100c::215 as permitted sender) smtp.mailfrom=donotreply@fms.treas.gov\r\nX-IronPort-AV: E=Sophos;i="5.38,392,1491264000"; \r\n   d="scan\'208,217";a="272129602"\r\nReceived: from kdm4.bpd.treas.gov ([10.112.34.10])\r\n  by in1mail.treasury.gov with ESMTP; 25 May 2017 18:19:44 +0000\r\nReceived: from pkbppss92 ([10.108.36.50])\r\n          by kdm4.bpd.treas.gov\r\n          with ESMTP id 2017052514194436-105240 ;\r\n          Thu, 25 May 2017 14:19:44 -0400 \r\nDate: Thu, 25 May 2017 14:19:44 -0400 (EDT)\r\nFrom: Bureau of the Fiscal Service-ITIM PP <donotreply@fms.treas.gov>\r\nTo: automatedotcnetuser+1212@gmail.com\r\nMessage-ID: <1312968258.1131495736384206.JavaMail.donotreply@fms.treas.gov>\r\nSubject: Account new password information\r\nMIME-Version: 1.0\r\nX-MIMETrack: Itemize by SMTP Server on KDM4/BPD at 05/25/2017 02:19:44 PM,\r\n\tSerialize by Router on KDM4/BPD at 05/25/2017 02:19:45 PM,\r\n\tSerialize complete at 05/25/2017 02:19:45 PM\r\nX-TNEFEvaluated: 1\r\nContent-Type: multipart/alternative; \r\n\tboundary="----=_Part_40_1120158404.1495736384202"\r\n\r\n------=_Part_40_1120158404.1495736384202\r\nContent-Transfer-Encoding: 7bit\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Disposition: inline\r\n\r\n\r\nThe following is your new password.\r\n\r\nProcess Reference: 4671898265331061783\r\n\r\nTemporary Password: [vI%49*J\r\nAccount Service: Single Sign On (FSLDAP)\r\nAccount Service Profile: FSLDAP Identity Profile\r\nOwner Name: otcnet tcnqeFIAS\r\nTime of service provision: May 25, 2017 02:19:43 EDT\r\n\r\n\r\n\r\n\r\n------=_Part_40_1120158404.1495736384202\r\nContent-Transfer-Encoding: 7bit\r\nContent-Type: text/html; charset=utf-8\r\nContent-Disposition: inline\r\n\r\n<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\r\n<head>\r\n    <title>IBM Tivoli Identity Manager Notification</title>  \r\n    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />\r\n    <link type="text/css" title="Styles" rel="stylesheet" href="https://ireg-pps.fms.treas.gov/itim/enrole/en/Styles.css" />\r\n</head>\r\n<body topmargin="0" marginheight="0" leftmargin="0" marginwidth="0" bgcolor="ffffff">\r\n<table width="100%" cellSpacing="0" cellPadding="0" border="0">\r\n    <tr>\r\n        <td bgcolor="white" rowspan="1" colspan="1"><img src="https://ireg-pps.fms.treas.gov/itim/enrole/en/images/logo.gif" alt="Tivoli Identity Manager - version 5.1" /></td>\r\n        <td align="right" bgcolor="white" rowspan="1" colspan="1"></td>\r\n    </tr>\r\n    <tr><td colspan="2" class="topnavigation" rowspan="1"><img border="0" align="left" width="5" height="1" src="https://ireg-pps.fms.treas.gov/itim/enrole/images/pixel.gif" /><img height="29" src="https://ireg-pps.fms.treas.gov/itim/enrole/images/pixel.gif" /><img border="0" width="14" height="1" src="https://ireg-pps.fms.treas.gov/itim/enrole/images/pixel.gif" /></td></tr>\r\n    <tr>\r\n        <td class="topheader" colspan="1" rowspan="1">\r\n            <table border="0" cellspacing="0" cellpadding="0">\r\n                <tr>\r\n                    <td height="36" width="100%" rowspan="1" colspan="1">IBM Tivoli Identity Manager Notification</td>\r\n                </tr>\r\n            </table>\r\n        </td>\r\n        <form action="https://ireg-pps.fms.treas.gov/itim/enrole/logon?TENANT_ID=FMS" method="GET" enctype="application/x-www-form-urlencoded">\r\n            <td class="topheader" colspan="1" align="RIGHT" rowspan="1">\r\n                <table border="0" cellspacing="0" cellpadding="0">\r\n                    <tr>\r\n                        <td height="36" width="100%" rowspan="1" colspan="1">\r\n                            <span class="submitLink">\r\n                            <input type="IMAGE" src="https://ireg-pps.fms.treas.gov/itim/enrole/en/images/login.gif" alt="Login to Identity Manager" onmouseover="this.src=\'https://ireg-pps.fms.treas.gov/itim/enrole/en/images/login_f2.gif\'" onmouseout="this.src=\'https://ireg-pps.fms.treas.gov/itim/enrole/en/images/login.gif\'" />\r\n                            &nbsp;&nbsp;                \r\n                            </span>\r\n                        </td>\r\n                    </tr>\r\n                </table>\r\n            </td>\r\n        </form>\r\n    </tr>\r\n    <tr>\r\n        <td colspan="2" class="login" width="100%" rowspan="1"><img border="0" height="36" width="1" src="https://ireg-pps.fms.treas.gov/itim/enrole/images/pixel.gif" /><br clear="none" />\r\n            <img align="left" border="0" height="100" width="15" src="https://ireg-pps.fms.treas.gov/itim/enrole/images/pixel.gif" />\r\n            <table border="0" cellspacing="0" cellpadding="0" width="100%">\r\n                <tr>\r\n                    <td align="left" class="content" rowspan="1" colspan="1">\r\n                    \r\n                    \r\n\r\nThe following is your new password.\r\n<p>\r\n<table width="98%" border="1" cellspacing="0" cellpadding="1">\r\n<tr><td class="content" rowspan="1" colspan="1">Process Reference:</td><td class="tablecell" rowspan="1" colspan="1">4671898265331061783</td></tr>\r\n\r\n<tr><td class="content" rowspan="1" colspan="1">Temporary Password:</td><td class="tablecell" rowspan="1" colspan="1">[vI%49*J</td></tr>\r\n<tr><td class="content" rowspan="1" colspan="1">Account Service:</td><td class="tablecell" rowspan="1" colspan="1">Single Sign On (FSLDAP)</td></tr>\r\n<tr><td class="content" rowspan="1" colspan="1">Account Service Profile:</td><td class="tablecell" rowspan="1" colspan="1">FSLDAP Identity Profile</td></tr>\r\n<tr><td class="content" rowspan="1" colspan="1">Owner Name:</td><td class="tablecell" rowspan="1" colspan="1">otcnet tcnqeFIAS</td></tr>\r\n<tr><td class="content" rowspan="1" colspan="1">Time of service provision:</td><td class="tablecell" rowspan="1" colspan="1">May 25, 2017 02:19:44 EDT</td></tr>\r\n\r\n\r\n</table>\r\n</p>\r\n\r\n\r\n                    \r\n                    </td>\r\n                </tr>\r\n            </table>\r\n            <br clear="none" /><img border="0" height="36" width="1" src="https://ireg-pps.fms.treas.gov/itim/enrole/images/pixel.gif" />\r\n        </td>\r\n    </tr>\r\n    <tr><td colspan="2" bgcolor="cccc99" height="9" rowspan="1"><img border="0" height="9" width="1" src="https://ireg-pps.fms.treas.gov/itim/enrole/images/pixel.gif" /></td></tr>\r\n    <tr><td colspan="2" class="copyright" rowspan="1">&copy; 1999-2005 IBM. All RIGHTS RESERVED.</td></tr>\r\n</table>\r\n</body>\r\n</html>\r\n------=_Part_40_1120158404.1495736384202--\r\n\r\n', b'SEQ': 15773}})
# [Finished in 2.6s]"""
# match = re.search(regex, tempPwd, flags=0)
# print ("Match at index %s, %s" % (match.start(), match.end()))
# . = any char
# \. = the actual dot character
# .? = .{0,1} = match any char zero or one times
# .* = .{0,} = match any char zero or more times
# .+ = .{1,} = match any char one or more times

# searches for email

search_string = "anish in a string anish again anish"

if re.search("anish", search_string):
    print("there is anish in string")

#  using find all - returns a list
all_anish = re.findall('anish', search_string)
for i in all_anish:
    print(i)

#  get iterator for all matching objects
for i in re.finditer("an.", search_string):
    loc_tuple = i.span()
    print(loc_tuple)
    # slice match
    print(search_string[loc_tuple[0]:loc_tuple[1]])


m = re.search(r'[\w.]+@[\w.]+', "blah nick.p@gmail.com")
print(m.group())


m = re.search(r'([\w.]+)@([\w.]+)', "blah nick.p@gmail.com")
print(m.group(0))
print(m.group(1))  # get username; 1 refers to 1st paranetheses
print(m.group(2))  # get domain

m = re.search(r'anish', "ANISH anish Ligy", flags=re.IGNORECASE)
print(m.group())

#  getting text from html code
text = """<!--
            <div id="footer">
                <p>Version: 1.2.0.0<br />Build Date: 2020-04-17 04:11 PM<br />
                </p>
            </div> --> 
            <p>Version: 1.2.0.0<br />Build Date: 2020-04-17 04:11 PM<br />
            """

pattern = r"(Version: .+)<br />(Build Date: .+)<br />"
import re

#  using match
match = re.search(pattern, text)
print(match.group(0))
print(match.group(1))
print(match.group(2))


# using findall
match = re.findall(pattern, text)
print(match)

#  naming matches
pattern = r"(?P<version>Version: .+)<br />(?P<build_date>Build Date: .+)<br />"
match = re.search(pattern, text)
print(match.group('version'))
print(match.group('build_date'))

# dates practice
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print ("Full match: %s" % (match))

# pwd extract
regex = r"[a-zA-Z]+ \d{1}"
regex = r'[A-Z]{1}[a-z]+[:\s]+[[.]+[\r]'
regex = r'Temporary Password:\s'
matches = re.findall(regex, "Thi guys: is 23 ye yeard Password: old!sfed Temporary Password: [vI%49*J\r")
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print ("Full match: %s" % (match))

 # FINAL - find pattern by searching every line
import re
pattern = re.compile(r'Password:') # provide pattern here
with open('Gmails.txt') as f:
    for line in f:
            if pattern.search(line):
                    print(line,end='')


#  FINAL - Findall method from file
# file = open("Gmails.txt", "r")
# regex = r"Password: (.*)" # get temp pwd
# matches = re.findall(regex, file.read())
# count = 0
# for match in matches:
# 	print (match)
# 	count = count + 1

# print("Total matches: {}".format(count))

# import re
# pattern = re.compile(r"""Perf frtst""")
# with open('Gmails.txt') as f:
#     for line in f:
#             if pattern.search(line):
#                     print(line,end='')



# import re
# pattern = re.compile("\d")

# for i, line in enumerate(open('Gmails.txt')):
#     for match in re.finditer(pattern, line):
#         print ('Found on line %s: %s' % (i+1, match.groups()))


# example showing usage of variables in reg expressions
# for key, value in UsersDict.items():
# 	try:
# 		file = open("Gmails.txt", "r")
# 		string = str(file.readlines())
# 		# regex = r"%s+.*" %s listofusers[i]
# 		# print(regex)
# 		usernamematch=re.search(r'{0}+.*'.format(value),string)
# 		try:
# 			newstring = usernamematch.group(0)
# 			pwdregex = r"Password:+..........." # get temp pwd
# 			matches = re.findall(pwdregex, newstring,re.MULTILINE)
# 			print(key.strip(),value.strip(), matches[0])
# 		except :
# 			print("***** Couldn't find user: ",key.strip(),value.strip())

# FINAL
# Users = {'pfrts009':'Perf frtstiJBNLk'}
# search metho
# for key, value in Users.items():
#
# 	file = open("Gmails.txt", "r")
# 	string = str(file.readlines())
# 	# regex = r"%s+.*" %s listofusers[i]
# 	# print(regex)
# 	usernamematch=re.search(r'{0}+.*'.format(value),string,re.MULTILINE)
# 	newstring = usernamematch.group(0)
# 	pwdregex = r"Password+..........." # get temp pwd
# 	matches = re.findall(pwdregex, newstring,re.MULTILINE)
# 	count = 0
# 	print(key,value, matches[0])
# for match in matches:
# 	print (match)
# 	count = count + 1
# print("Total matches: {}".format(count))

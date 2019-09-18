#              ID    First Name     Last Name
line_record = "2        John         Smith"

ID = slice(0, 8)
FIRST_NAME = slice(9, 21)
LAST_NAME = slice(22, 27)

name = f"{line_record[FIRST_NAME].strip()} {line_record[LAST_NAME].strip()}"
print(name)

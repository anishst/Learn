import re
import time


def validate_date_value(date_text):
    """expected format MM/DD/YYYY"""
    try:
        valid_date = time.strptime(date_text, '%m/%d/%Y')
        # print(f"{date_text} is valid date!")
        return True
    except ValueError:
        # print(f"{date_text} is Invalid date!")
        return False


date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
date_list = [
    '67/03/1982',
    '03/03/2000'
]

# The date format must be MM/DD/YYYY.
for date in date_list:
    if date_pattern.match(date) and validate_date_value(date):
        print(f"{date} is valid format")
        validate_date_value(date)
    else:
        print(f"{date} is invalid format")

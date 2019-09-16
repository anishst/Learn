string = """
otcnqe09, you must change your password before continuing. You will not be permitted to use your account until you have completed this activity.

 
NOTE: The new password must satisfy the following requirements:
Must be at least 12 characters long.
Must contain at least one uppercase letter.
Must contain at least one lowercase letter.
Must contain at least one numeric character.
Must contain at least one special character.
Must not have more than two repeating characters.
Must not repeat any of your last ten passwords.
Must not have been your password in during the last ten days.
Must not be a word in a language, slang, dialect, or jargon.
Must not be related to personal identity, history, environment, or other personal associations.
Must not be shared or displayed in plain view.
04-10-2019 12:04:16 PM - TestUserAccounts - INFO: test_ISIM_test_user_login_check.py: 41: otcnqe09, you must change your password before continuing. You will not be permitted to use your account until you have completed this activity.

 
NOTE: The new password must satisfy the following requirements:
Must be at least 12 characters long.
Must contain at least one uppercase letter.
Must contain at least one lowercase letter.
Must contain at least one numeric character.
Must contain at least one special character.
Must not have more than two repeating characters.
Must not repeat any of your last ten passwords.
Must not have been your password in during the last ten days.
Must not be a word in a language, slang, dialect, or jargon.
Must not be related to personal identity, history, environment, or other personal associations.
Must not be shared or displayed in plain view.

"""

try:
    login_error_msg_text = string
    # print(login_error_msg_text)
    if "you cannot access your account because you have exceeded the limit of login attempts" in login_error_msg_text:
        failure_reason = "EXCEEDED LOGIN ATTEMPTS"
        print(failure_reason)
    elif "You entered an invalid User Id and Password combination." in login_error_msg_text:
        failure_reason = 'INVALID USER ID AND PASSWORD'
        print(failure_reason)
    elif " your account has been disabled by a Security Administrator." in login_error_msg_text:
        failure_reason = "ACCOUNT IS DISABLED"
        print(failure_reason)
    elif "you must change your password before continuing" in login_error_msg_text:
    	failure_reason = 'CHANGE PASSWORD'
    	print(failure_reason)
    else:
        failure_reason = "UNKNOWN"
        print(failure_reason)
except Exception as e:
    print(f'Unable to read the error {e}')
    failure_reason = "UNKNOWN"
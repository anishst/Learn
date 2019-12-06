from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

print(bcrypt.generate_password_hash('testpwd'))
# output example: b'$2b$12$TccesgIjmmccnrn3ZuIA2OlvyQ/WeU5uxFs4TmEhGFfK/qT2cOI5.'

# get convert byte format to string
print(bcrypt.generate_password_hash('testpwd').decode('utf-8'))
# output example: $2b$12$6tv77QSv2cewwEGiyywmZOwkSRWwtuV9gzvljhcxaQZfE7e0gXiOu

# store in var
hashed_pwd = bcrypt.generate_password_hash('testpwd').decode('utf-8')
# checing password

# check using wrong pwd
print(bcrypt.check_password_hash(hashed_pwd, 'password'))
# output = False

# check using correct pwd
print(bcrypt.check_password_hash(hashed_pwd, 'testpwd'))
# output = True
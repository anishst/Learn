users = {
    (0, "anish", "password"),
    (1, "ligy", "password"),
    (2, "leah", "password"),
}

username_mapping = {user[1]: user for user in users}
print(username_mapping) 

# get a specific user info
print(username_mapping['ligy'])

username_input = input("Enter username: ")
pwd_input = input("Enter password: ")

_, username, password = username_mapping[username_input]

if pwd_input == password:
    print("pwd correct")
else:
    print("pwd incorrect")
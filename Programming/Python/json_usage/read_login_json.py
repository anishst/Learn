import json

# open json file
with open('login_info.json') as file:
    login_data = json.load(file)


print(login_data)
print(login_data["ONLINE"]["QAEC"]["HLAS"])

user_id, password = login_data["ONLINE"]["QAEC"]["HLAS"]
print(user_id, password)

user_id, password = login_data["ONLINE"]["QAEF"]["HLAS"]
print(user_id, password)

def get_online_info(env, rolename):
    print(login_data["ONLINE"][env][rolename])

get_online_info('QAEF','HLAS')
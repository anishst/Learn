# https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#for-secret-text-usernames-and-passwords-and-secret-files
import json, os
# Read the file - for testing read from json
#  read file using local var 'FILE'
with open(os.getenv('FILE')) as config_file:
    config = json.load(config_file)
    print(config['browser'])
    print(config['Password'])

#  read json file using env var
with open(os.getenv('json_file')) as config_file:
    config = json.load(config_file)
    print(config['browser'])
    print(config['Password'])
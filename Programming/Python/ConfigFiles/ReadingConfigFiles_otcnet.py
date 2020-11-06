# https://github.com/dabeaz/python-cookbook/tree/8a71861a81350e55bd77556996ac3b530a1ffe5e/src/13/reading_configuration_files

from configparser import ConfigParser

cfg = ConfigParser()

cfg.read('ConfigFile_otcnet.ini')

print (cfg.sections())

print(cfg.get('TestCaseRelated','browser'))
print(cfg.get('TestCaseRelated','close_browsers_before_run'))

print(cfg.get('TestCaseRelated','url'))

print("Looping thru values...")
key_to_search = 'url'
value = ""

for each_section in cfg.sections():
    for (each_key, each_val) in cfg.items(each_section):
        if key_to_search == each_key:
            print("found")
            value = each_val
            break
            
print(key_to_search, value)
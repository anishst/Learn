# https://github.com/dabeaz/python-cookbook/tree/8a71861a81350e55bd77556996ac3b530a1ffe5e/src/13/reading_configuration_files

from configparser import ConfigParser

cfg = ConfigParser()

cfg.read('ConfigFile.ini')

print (cfg.sections())

print(cfg.get('debug','log_errors'))
print(cfg.get('server','port'))
print(cfg.get('Env','url'))

# https://docs.python.org/3/library/logging.html
import logging

# 5 levels: DEBUG, INFO, WARNING (Default), ERROR, CRITICAL
# https://docs.python.org/3/library/logging.html#logrecord-attributes
FORMAT = '%(asctime)s:%(levelname)s:%(message)s:%(module)s:%(filename)s:%(filename)s'
logging.basicConfig(filename='test.log',level=logging.INFO,format=FORMAT)

def divide(x,y):
    return x /y

num1 = 5
num2 = 0


try:
    div_result = divide(num1,num2)
    print(div_result)
    logging.info(div_result)
except Exception as e:
    print("there was error: {}".format(e))
    logging.error(e)




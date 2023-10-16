from socket import *
from sqlalchemy import create_engine, event
from datetime import datetime
from subprocess import call
 
import urllib
import pandas as pd
import psutil
import pyodbc
import numpy as np


ser = socket( AF_INET, SOCK_STREAM )

ser.bind(('192.168.56.1', 7000))

ser.listen(20)


user, addr = ser.accept()
print(f"Conected \n{user} \n{addr}\n")


penis=psutil.virtual_memory().percent
xyi=psutil.cpu_percent(interval=None, percpu=False)
print(f'\n percent={xyi} \n')
print(f'\n {penis} \n')

user.send(f'Gpu using stats percent={penis} CPU using stats percent={xyi} I am your Father conected \n{user} \n{addr}\n'.encode('utf-8'))
user.send(f'\n\n\n\n\n percent={penis}'.encode('utf-8'))
user.send(f'\n\n\n\n\n\n\n percent={xyi}'.encode('utf-8'))

#user.send(f'\n \n CPU using stats {xyi}'.encode('utf-8'))
# user.send(f'CPU using stats {xyi}'.encode('utf-8'))
# user.send('I am your Father'.encode('utf-8'))


mag = user.recv(10240).decode('utf-8')

print(f'User  message: \n\t{mag}')






#while True:

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


penis=psutil.virtual_memory()
xyi=psutil.cpu_times()
print(f'\n {xyi} \n')
print(f'\n {penis} \n')

user.send('I am your Father'.encode('utf-8'))


mag = user.recv(10240).decode('utf-8')

print(f'User  message: \n\t{mag}')





#while True:

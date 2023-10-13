from sqlalchemy import create_engine, event
from datetime import datetime
from subprocess import call
 
import urllib
import pandas as pd
import psutil
import pyodbc
import numpy as np

from socket import *


ser = socket( AF_INET, SOCK_STREAM )

ser.bind(('192.168.56.1', 7000))

ser.listen(5)


user, addr = ser.accept()
print(f"Conected \n{user} \n{addr}\n")

user.send('I am your Father'.encode('utf-8'))


mag = user.recv(1024).decode('utf-8')

print(f'User  message: \n\t{mag}')

def RecordMetrics():
 
    # dataabase connection - assign to the correct values
    driver = '{SQL Server}'
    server = ''
    user = ''
    password = ''
    database = ''
    table = 'ServerMonitoring'
 
    params = urllib.parse.quote_plus(r'DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(driver, server, database, user, password))
    conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    engine = create_engine(conn_str)
 
    # gets the disk partitions in order to get a list of NFTS drives
    drps = psutil.disk_partitions()
    drives = [dp.device for dp in drps if dp.fstype == 'NTFS']
 
    # initialises the data frame with the appropriate values
    df = pd.DataFrame(
        {
            'CPU': [psutil.cpu_percent()],
            'VirtualMemory': [psutil.virtual_memory()[2]],
            'LastBootedAt' : datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
        })
 
    # records the drive usage for each drive found
    for drive in drives:
        df['{}_DriveUsage'.format(drive.replace(":\\",""))] = psutil.disk_usage(drive)[3]
 
    # adds the current date and time stamp
    df['LoadDate'] = datetime.now()
     
    #if_exists="replace" if the table does not yet exist, then add HistoryID (or ID) as the auto-incremented primary key
    df.to_sql(table, engine, if_exists="append", index=False)


def CheckCPU():
     
    df_CPU = df.read_sql('SELECT TOP(5) CPU FROM dbo.ServerMonitoring ORDER BY LoadDate DESC', conn_str)
     
    avg_CPU = df_CPU['CPU'].mean()
     
    # if the CPU Average is above 90%
    if avg_CPU > 90:
         
        print('High CPU Usage Detected: {}%'.format(round(avg_CPU,2)))       
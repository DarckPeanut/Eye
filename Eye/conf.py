from socket import *
from index.py import entery_get_ip
from index.py import entery_get_port

cli = socket(AF_INET, SOCK_STREAM)

cli.connect((f'{entery_get_ip}', entery_get_port)) #Нужны переменные которым будет передоваться инфа от полей ввода.

data = cli.recv( 1024 )
mag = data.decode('utf-8')

print(f'Server message: \n\t{mag}')

cli.send('SLAAAY'.encode('utf-8'))

input('End operation') 
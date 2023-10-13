from socket import *
import requests


cli = socket(AF_INET, SOCK_STREAM)

cli.connect((f'192.168.56.1', 7000)) #Нужны переменные которым будет передоваться инфа от полей ввода.

data = cli.recv( 1024 )
mag = data.decode('utf-8')


print(f'Server message: \n\t{mag}')

cli.send('SLAAAY'.encode('utf-8'))

res = cli.requests.post(data={'st3': 'jim hopper'})
print(res.text)


input('End operation') 
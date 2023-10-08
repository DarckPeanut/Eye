from socket import *


cli = socket(AF_INET, SOCK_STREAM)

cli.connect(('192.168.56.1', 7000))

data = cli.recv( 1024 )
mag = data.decode('utf-8')

print(f'Server message: \n\t{mag}')

cli.send('SLAAAY'.encode('utf-8'))

input('End operation') 
from socket import *


ser = socket( AF_INET, SOCK_STREAM )

ser.bind(('192.168.56.1', 7000))

ser.listen(5)


user, addr = ser.accept()
print(f"Conected \n{user} \n{addr}\n")

user.send('I am your Father'.encode('utf-8'))


mag = user.recv(1024).decode('utf-8')

print(f'User  message: \n\t{mag}')


#while True:

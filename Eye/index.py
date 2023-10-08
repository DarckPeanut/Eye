from tkinter import *
from tkinter import ttk
from socket import *
import runpy

from datetime import datetime
from subprocess import call
 
import pandas as pd
import psutil
import numpy as np




root1 = Tk()     # создаем корневой объект - окно
root1.title("Eye")     # устанавливаем заголовок окна
root1.geometry("700x700")# устанавливаем размеры окна
root1['bg']=['grey8']

style=ttk.Style().configure("TLabel",  font="helvetica 13", foreground="green", padding=8, background="grey8")


ttk.Label(text="Fill blanks with server IP and Port").pack(anchor=NW, padx=0)

ttk.Label(text='IP').pack( anchor=NW, pady=10)
ip_opener = ttk.Entry().pack(anchor=NW, pady=10, padx=20 )
ip_get= Entry().get()


ttk.Label(text='PORT').pack(anchor=NW, pady=5, padx=0)
port_opener = ttk.Entry().pack(anchor=NW, pady=10, padx=20 )
7000== Entry().get()









def click_btn_first():
	print('GEY')
	
	class Client():
		cli = socket(AF_INET, SOCK_STREAM)

		cli.connect(("192.168.56.1", 7000)) #Нужны переменные которым будет передоваться инфа от полей ввода.

		data = cli.recv( 1024 )
		mag = data.decode('utf-8')

		print(f'Server message: \n\t{mag}')

		cli.send('SLAAAY'.encode('utf-8'))

		input('End operation') 


btn=Button(text='Подключится',background="grey12", border = 0, font="helvetica 13", foreground="green", command=click_btn_first)
btn.pack(anchor=SW, pady=10, padx=10,)

	


class Index_Py():

	value_var_1 = IntVar(value=30)  #сноска на значение x переменной загрузки cpu после запроса
	value_var = IntVar(value=45)

	#Style And Text

	ttk.Style().configure("TLabel",  font="helvetica 13", foreground="green", padding=8, background="grey8")

	ttk.Label(text="Server to user info").pack(padx=50,side=TOP, pady=20)				#Name


	ttk.Label(text="CPU Progressbar").pack(anchor=SE, padx=[20, 50], pady=[30,0]) 					#CPU
	ttk.Progressbar(orient='horizontal', length=200, variable=value_var).pack( anchor=SE, padx=20,)
	ttk.Label(text="CPU Progressbar", textvariable=value_var).pack(anchor=SE, padx=[0,180])


	ttk.Label(text="RAM Progressbar").pack(anchor=SE,padx=[20,50], pady=[50,0]) 					#RAM
	ttk.Progressbar(orient='horizontal', length=200, variable=value_var_1).pack(anchor=SE, padx=20,)
	ttk.Label(text="RAM Progressbar", textvariable=value_var_1).pack(anchor=SE,  padx=[0,180])



root1.mainloop()
from tkinter import *
from tkinter import ttk
#from conf.py import xxx



class Index_Py():

	root1 = Tk()     # создаем корневой объект - окно
	root1.title("Eye")     # устанавливаем заголовок окна
	root1.geometry("700x450")# устанавливаем размеры окна
	root1['bg']=['grey8']




	value_var_1 = IntVar(value=30)  #сноска на значение x переменной загрузки cpu после запроса
	value_var = IntVar(value=45)

	#Style And Text

	ttk.Style().configure("TLabel",  font="helvetica 13", foreground="green", padding=8, background="grey8")

	ttk.Label(text="Server to user info").pack(padx=50, pady=20)				#Name


	ttk.Label(text="CPU Progressbar").pack(anchor=SE, padx=[20, 50], pady=[30,0]) 					#CPU
	ttk.Progressbar(orient='horizontal', length=200, variable=value_var).pack( anchor=SE, padx=20,)
	ttk.Label(text="CPU Progressbar", textvariable=value_var).pack(anchor=SE, padx=[0,180])


	ttk.Label(text="CPU Progressbar").pack(anchor=SE, padx=[20,50], pady=[50,0]) 					#RAM
	ttk.Progressbar(orient='horizontal', length=200, variable=value_var_1).pack( anchor=SE, padx=20,)
	ttk.Label(text="CPU Progressbar", textvariable=value_var_1).pack(anchor=SE, padx=[0,180])



	#Создать окно с приветствием и просьбой вбить адрес  и порт сервера. Дальше открытие новго окна где видны все подключения сервера и общая нагруженность его процессоров в виде строк действия


	#Progress Bars and buttons



	#ttk.Label(text="Hello World!").pack(pady=100, padx=100)
	#ttk.Label(text="Bye World..").pack()
 
	root1.mainloop()
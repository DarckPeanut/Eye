from tkinter import *
from tkinter import ttk

root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("700x450")# устанавливаем размеры окна
root['bg']=['grey8']






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






#Progress Bars and buttons



#ttk.Label(text="Hello World!").pack(pady=100, padx=100)
#ttk.Label(text="Bye World..").pack()
 
root.mainloop()
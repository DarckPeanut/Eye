from tkinter import *
from tkinter import ttk

root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("700x450")# устанавливаем размеры окна
root['bg']=['grey8']







#Style And Text

ttk.Style().configure("TLabel",  font="helvetica 13", foreground="green", padding=8, background="grey8")

ttk.Label(text="Server to user info").pack(padx=50, pady=20)
ttk.Label(text="CPU Progressbar").pack(anchor=SE, padx=20)






#Progress Bars and buttons

value_var = IntVar(value=30)#сноска на значение x переменной загрузки cpu после запроса

ttk.Progressbar(orient='horizontal', length=200, variable=value_var).pack( anchor=SE, padx=20,)

#ttk.Label(text="Hello World!").pack(pady=100, padx=100)
#ttk.Label(text="Bye World..").pack()
 
root.mainloop()
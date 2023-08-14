from tkinter import *
from tkinter import ttk

root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("700x450")# устанавливаем размеры окна

ttk.Style().configure("TLabel",  font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB")


ttk.Label(text="Hello World!").pack()
ttk.Label(text="Bye World..").pack()
 
root.mainloop()
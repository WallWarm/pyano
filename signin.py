import mysql.connector
from tkinter import *
from tkinter import messagebox
o = mysql.connector.connect(user = 'root', password = 'root', host = 'localhost', database = 'authdb')
curo = o.cursor()

def su():
    user = uname.get()
    pwd = pword.get()

    if user == '' or pwd == '':
        messagebox.showerror('Error','Both username and password are required.')
        su()
    curo.execute('select * from users where username = %s',(user,))
    if curo.fetchall() == True:
        messagebox.showerror('Error','This username is taken.')
        su()
    curo.execute('insert into users values(%s,%s)',(user,pwd))
    messagebox.showinfo('Success','Signed up successfully!')

def si():
    user = uname.get()
    pwd = pword.get()

    if user == '' or pwd == '':
        messagebox.showerror('Error','Both username and password are required.')
        su()
    curo.execute('select * from users where username = %s and password = %s',(user,pwd))
    if curo.fetchall() == True:
        messagebox.showinfo('Success','Welcome {username}!')
        su()
    else:
        messagebox.showerror('Error','Invalid name / password')


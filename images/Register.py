import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import bcrypt

#--mySqlinit
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbactivity6"
)
cursor = conn.cursor()
#--mySqlinit




root= tk.Tk()

frame = tk.Frame(root, width="450", height="400")
root.resizable(False,False)

#---Label
title=tk.Label(root,  text="Register Account", font=('Arial',20,'bold'))
title.place(x=100,y=0)

unamelbl=tk.Label(root,  text="Username", font=('Arial',14))
unamelbl.place(x=15,y=50)

passWlbl=tk.Label(root,  text="Password", font=('Arial',14))
passWlbl.place(x=15,y=100)

orgPoslbl=tk.Label(root,  text="Confirm Password", font=('Arial',14))
orgPoslbl.place(x=15,y=150)

confPasslbl=tk.Label(root,  text="Email", font=('Arial',14))
confPasslbl.place(x=15,y=200)

loginlbl=tk.Label(root,  text="Login", font=('Arial',10), fg='blue')
loginlbl.place(x=250,y=320)

succlbl=tk.Label(root,  text="", font=('Arial',12))
succlbl.place(x=150,y=350)
#---Label


#--Fields
uNameInp = tk.Entry(root, width=30)
uNameInp.place(x=175,y=55)

passInp = tk.Entry(root, show='*',width=30)
passInp.place(x=175,y=105)

confpassInp = tk.Entry(root, show='*',width=30)
confpassInp.place(x=175,y=155)

#--Fields

#--ListBox

email = tk.Entry(root, width=30)
email.place(x=175,y=210)


#--ListBox

#--Button command


def storeInps():
    passWord=bcrypt.hashpw(passInp.get().encode(), bcrypt.gensalt())  
    userName=uNameInp.get()
    emailVal=email.get()
    if((passInp.get() == confpassInp.get()) and passInp.get()!=""):
        sql = "INSERT INTO `tbluser` (`username`, `password`, `email`, `pfp`, `userid`) VALUES (%s,%s, %s,'default.png', NULL)"
        cursor.execute(sql,(userName,passWord,emailVal))
        conn.commit()
        print(userName)
        print(passWord)
        print(emailVal)  
        uNameInp.delete(0, tk.END)
        passInp.delete(0, tk.END)
        confpassInp.delete(0, tk.END)
        succlbl.configure(text="Register Successful!!", fg='green')
    else:
       succlbl.configure(text="Inputted passwords do not match", fg='red')

#--Button
regBtn= tk.Button(root,text="Register", width=15, command=storeInps)
regBtn.place(x=100, y=320)
#--Button


def switch_window(event):  # Add an optional argument
    root.withdraw()
    import LoginWindow
    LoginWindow.root.deiconify()
loginlbl.bind('<Button-1>',switch_window)

frame.pack()




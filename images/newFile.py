import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import bcrypt
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbactivity6"
)
cursor = conn.cursor()
root =tk.Tk()
searchlbl = tk.Label(root, text="Search User")
searchlbl.grid(row=2, column=0, sticky="W")

search = tk.Entry(root, width=30)
search.grid(row=2, column=1, sticky="W")
global pfp
pfp = tk.Label(root)
newpfp = tk.Label(root, text="new pfp file")
newpfpfile=tk.Entry(root, width=30)
def show_image(row4):
    print(row4)
    img = Image.open(row4)
    img = img.resize((75, 75), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(image=img)
    pfp.img_tk = img_tk  # store the PhotoImage object as an attribute of the label widget
    pfp.config(image=img_tk)

def searchResult():
    
    sql = "SELECT * FROM tbluser WHERE `username` = %s"
    val=search.get()
    cursor.execute(sql,(val,))
    rows = cursor.fetchone()
    
    print(rows)
    if rows is not None:
        
        show_image(rows[4])
        pfp.grid(row=4, column=1, sticky="NSEW")
        
        


searchBtn= tk.Button(root,text="search", width=10, command=searchResult)
searchBtn.grid(row=2, column=2, sticky="W")   

root.mainloop()
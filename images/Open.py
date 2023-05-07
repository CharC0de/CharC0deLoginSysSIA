import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import bcrypt
conn = mysql.connector.connect(
  host="localhost",
  user="child",
  password="",
  database="dbactivity6"
)

    


cursor = conn.cursor()

child = tk.Tk()



welcome= tk.Label(child, text="Dashboard")
welcome.grid(row=0, column=0, sticky="W")


logoutlbl=tk.Label(child,  text="Logout", font=('Arial',10), fg="blue")
logoutlbl.grid(row=0, column=3, sticky="NSEW")

searchlbl = tk.Label(child, text="Search User")
searchlbl.grid(row=2, column=0, sticky="W")

search = tk.Entry(child, width=30)
search.grid(row=2, column=1, sticky="W")


def reset_window():
    dataNo.grid_forget()
    picture.grid_forget()
    name.grid_forget()
    password.grid_forget()
    newpassword.grid_forget()
    newpfp.grid_forget()
    email.grid_forget()
    pkRes.grid_forget()
    pfp.grid_forget()
    userRes.delete(0, tk.END)
    userRes.grid_forget()
    newpass.delete(0, tk.END)
    newpass.grid_forget()
    oldpass.delete(0, tk.END)
    oldpass.grid_forget()
    emailRes.delete(0, tk.END)
    emailRes.grid_forget()
    newpfpfile.delete(0, tk.END)
    newpfpfile.grid_forget()
    uploadBtn.grid_forget()
    updateBtn.grid_forget()
    deleteBtn.grid_forget()
    
    
def switch_to_second_window(event):
    child.withdraw()
    reset_window()
    import LoginWindow as login
    login.child.deiconify()


logoutlbl.bind('<Button-1>',switch_to_second_window)

def updateData(username,image,newpassword,oldpassword,dbpassword,email,id):
    if (len(newpassword)<=1 and len(image)<=1):
        sql="UPDATE `tbluser` SET `username` = %s, `email` = %s WHERE `tbluser`.`userid` = %s"
        cursor.execute(sql,(username,email,id))
        conn.commit()
        reset_window()
    elif(len(newpassword)<=1 or len(image)<=1):
        if(len(image)<=1):
            if(bcrypt.checkpw(oldpassword.encode('utf-8'),dbpassword.encode('utf-8'))):
                hashedP=bcrypt.hashpw(oldpassword.encode(), bcrypt.gensalt())
                sql="UPDATE `tbluser` SET `username` = %s, `email` = %s,`password` = %s WHERE `tbluser`.`userid` = %s"
                cursor.execute(sql,(username,email,hashedP,id))
                conn.commit()
                reset_window()
        if(len(newpassword)<=1):
            sql="UPDATE `tbluser` SET `username` = %s, `email` = %s,`pfp` = %s WHERE `tbluser`.`userid` = %s"
            cursor.execute(sql,(username,email,image,id))
            conn.commit()
            reset_window()

def deleteData(row0):
    sql="DELETE FROM `tbluser` WHERE `tbluser`.`userid` = %s"
    cursor.execute(sql,(row0,))
    conn.commit()
    reset_window()


dataNo = tk.Label(child, text="User ID")
picture = tk.Label(child, text="Picture")
name = tk.Label(child, text="Username")
email = tk.Label(child, text="Email")
password = tk.Label(child, text="Old Password")
newpassword = tk.Label(child, text="New Password")
pkRes = tk.Label(child, text="")
userRes = tk.Entry(child, width=30)
newpass = tk.Entry(child, show="*")
oldpass = tk.Entry(child, show="*")
emailRes = tk.Entry(child, width=30)
uploadBtn= tk.Button(child,text="upload", width=10)
updateBtn= tk.Button(child,text="update", width=10)
deleteBtn= tk.Button(child,text="delete", width=10, fg="red")
global pfp
pfp = tk.Label(child)
newpfp = tk.Label(child, text="new pfp file")
newpfpfile=tk.Entry(child, width=30)

def show_image(row4):
    print(row4)
    img = Image.open(row4)
    img = img.resize((75, 75), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    pfp.image = img_tk  # assign directly to pfp's image option
    pfp.config(image=img_tk)

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        global file_name
        file_name = os.path.basename(file_path)
        print("Selected file:", file_name)
        newpfpfile.insert(0,file_name)
        save_file_dialog(file_path, img)

def save_file_dialog(file_path, img):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(dir_path, os.path.basename(file_path))
    save_path = filedialog.asksaveasfilename(initialdir=dir_path, initialfile=os.path.basename(file_path), defaultextension='.jpg')
    if save_path:
        img.save(save_path)

def searchResult():
    reset_window()
    sql = "SELECT * FROM tbluser WHERE `username` = %s"
    val=search.get()
    cursor.execute(sql,(val,))
    rows = cursor.fetchone()
    print(rows)
    if rows is not None:
        
        dataNo.config(text="ID.", fg="black")
        dataNo.grid(row=3, column=0, sticky="NSEW")
        picture.grid(row=3, column=1, sticky="NSEW")
        name.grid(row=3, column=2, sticky="NSEW")
        email.grid(row=3, column=3, sticky="NSEW")
        password.grid(row=3, column=4, sticky="NSEW")
        newpassword.grid(row=3, column=5, sticky="NSEW")
        newpfp.grid(row=3, column=6, sticky="NSEW")

        

        pkRes.config(text=rows[0])
        pkRes.grid(row=4, column=0, sticky="NSEW")
        
        show_image(rows[4])
        pfp.grid(row=4, column=1, sticky="NSEW")
        
        userRes.insert(0,rows[1])
        userRes.grid(row=4, column=2, sticky="W")
        
        emailRes.insert(0,rows[3])
        emailRes.grid(row=4, column=3, sticky="NSEW")
        
        newpass.grid(row=4, column=4, sticky="W")
        oldpass.grid(row=4, column=5, sticky="W")
        newpfpfile.grid(row=4, column=6, sticky="W")
        
        
        uploadBtn.grid(row=4, column=7, sticky="W")
        deleteBtn.grid(row=4, column=9, sticky="W")
        updateBtn.grid(row=4, column=8, sticky="W")
        
        uploadBtn.config(command=open_file_dialog)
        updateBtn.config(command=lambda: updateData(userRes.get(),emailRes.get(),newpass.get(),oldpass.get(),file_name,rows[0]))
        deleteBtn.config(command=lambda: deleteData(rows[0]))
    else:
        dataNo.config(text="User does not exist", fg="red")
        dataNo.grid(row=3, column=0, sticky="W")
      


searchBtn= tk.Button(child,text="search", width=10, command=searchResult)
searchBtn.grid(row=2, column=2, sticky="W")   


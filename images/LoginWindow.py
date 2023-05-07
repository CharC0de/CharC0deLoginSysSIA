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

frame = tk.Frame(root,width=400,height=200)
#---Label
title=tk.Label(root,  text="Login System", font=('Arial',20,'bold'))
title.place(x=100,y=0)

unamelbl=tk.Label(root,  text="Username", font=('Arial',14))
unamelbl.place(x=25,y=50)

passWlbl=tk.Label(root,  text="Password", font=('Arial',14))
passWlbl.place(x=25,y=100)

regLnklbl=tk.Label(root,  text="Register Here", font=('Arial',10), fg="blue")
regLnklbl.place(x=275,y=130)

succLabel=tk.Label(root,  text="", font=('Arial',12))
succLabel.place(x=150,y=175)
#---Label


#--Fields
unameInp = tk.Entry(root, width=30)
unameInp.place(x=125,y=55)

passInp = tk.Entry(root, show='*',width=30)
passInp.place(x=125,y=105)
#--Fields

#--Button
submitBtn= tk.Button(root,text="Login", width=15)
submitBtn.place(x=150, y=130)
#--Button
frame.pack()



#--backend
def switch_to_second_window(event):  
    root.withdraw() 
    Register()
    
regLnklbl.bind('<Button-1>',switch_to_second_window)



def loginAcc():
    userName=unameInp.get()
    print(userName)
    sql = "SELECT * FROM `tbluser` WHERE `username` = %s"
    cursor.execute(sql,(userName,))
    row=cursor.fetchone()
    print(row is not None)
    if row is not None:  
        print(row[1].encode('utf-8'))

        if(bcrypt.checkpw(passInp.get().encode('utf-8'),row[2].encode('utf-8'))):
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print(row[4])
            unameInp.delete(0, tk.END)
            passInp.delete(0, tk.END)
            succLabel.config(text="Authorized Access", fg='green')
            root.withdraw() 
            Open()
        else:
            succLabel.config(text="Invalid user input", fg='red')
    else:
        succLabel.config(text="Invalid user input", fg='red')
    
        
submitBtn.config(command=loginAcc)




def Open():
    child = tk.Toplevel(root)



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
        root.deiconify()
        reset_window()

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
    emailRes = tk.Entry(child)
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
            emailRes.grid(row=4, column=3, sticky="W")
            
            newpass.grid(row=4, column=4, sticky="W")
            oldpass.grid(row=4, column=5, sticky="W")
            newpfpfile.grid(row=4, column=6, sticky="W")
            
            
            uploadBtn.grid(row=4, column=7, sticky="W")
            deleteBtn.grid(row=4, column=9, sticky="W")
            updateBtn.grid(row=4, column=8, sticky="W")
            
            uploadBtn.config(command=open_file_dialog)
            updateBtn.config(command=lambda: updateData(userRes.get(),file_name,newpass.get(),oldpass.get(),rows[2],emailRes.get(),rows[0]))
            deleteBtn.config(command=lambda: deleteData(rows[0]))
        else:
            dataNo.config(text="User does not exist", fg="red")
            dataNo.grid(row=3, column=0, sticky="W")
        


    searchBtn= tk.Button(child,text="search", width=10, command=searchResult)
    searchBtn.grid(row=2, column=2, sticky="W")

def Register():
    child1= tk.Toplevel(root)

    frame = tk.Frame(child1, width="450", height="400")
    child1.resizable(False,False)

    #---Label
    title=tk.Label(child1,  text="Register Account", font=('Arial',20,'bold'))
    title.place(x=100,y=0)

    unamelbl=tk.Label(child1,  text="Username", font=('Arial',14))
    unamelbl.place(x=15,y=50)

    passWlbl=tk.Label(child1,  text="Password", font=('Arial',14))
    passWlbl.place(x=15,y=100)

    orgPoslbl=tk.Label(child1,  text="Confirm Password", font=('Arial',14))
    orgPoslbl.place(x=15,y=150)

    confPasslbl=tk.Label(child1,  text="Email", font=('Arial',14))
    confPasslbl.place(x=15,y=200)

    loginlbl=tk.Label(child1,  text="Login", font=('Arial',10), fg='blue')
    loginlbl.place(x=250,y=320)

    succlbl=tk.Label(child1,  text="", font=('Arial',12))
    succlbl.place(x=150,y=350)
    #---Label


    #--Fields
    uNameInp = tk.Entry(child1, width=30)
    uNameInp.place(x=175,y=55)

    passInp = tk.Entry(child1, show='*',width=30)
    passInp.place(x=175,y=105)

    confpassInp = tk.Entry(child1, show='*',width=30)
    confpassInp.place(x=175,y=155)

    #--Fields

    #--ListBox

    email = tk.Entry(child1, width=30)
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
    regBtn= tk.Button(child1,text="Register", width=15, command=storeInps)
    regBtn.place(x=100, y=320)
    #--Button


    def switch_window(event):  # Add an optional argument
        child1.withdraw()
        root.deiconify()
    loginlbl.bind('<Button-1>',switch_window)

    frame.pack()







root.resizable(False,False)
root.mainloop()
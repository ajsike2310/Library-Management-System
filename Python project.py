import mysql.connector
import random
import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox
from PIL import ImageTk#python imaging library
from datetime import date,datetime
mydb=mysql.connector.connect (host="localhost",user="root", passwd="12345")
myc=mydb.cursor()
def createdatabase():
    myc.execute("create database if not exists Library1")
    myc.execute("use Library1")
def createtables():
    myc.execute("create table if not exists Library (bookNo int primary key,Name varchar(50),Quantity int);")
    myc.execute("create table if not exists member (mid int primary key,Name varchar(50),age int,doe varchar(50),type varchar(50));")
    myc.execute("create table if not exists login (Empno int primary key,password varchar(50),Name VARCHAR(50));")
    myc.execute("create table if not exists Employee (Empno int Primary key,password varchar(50),Name VARCHAR(50),Position varchar(50),Salary int,gmail varchar(50), MobileNo bigint);")
    myc.execute("truncate table login")
    insert()
def insert():
    myc.execute("Select * from Employee")
    k=myc.fetchall()
    if k==[]:
        myc.execute("INSERT INTO Employee VALUES (112233, 'Emily@2020', 'Emily Watson', 'Librarian', 7000, 'emilywatson@gmail.com', 9871234560)")
        myc.execute("INSERT INTO Employee VALUES (223344, 'James1985', 'James Turner', 'Assistant Librarian', 6500, 'jturner85@gmail.com', 8762345671)")
        myc.execute("INSERT INTO Employee VALUES (334455, 'Sarah@lib', 'Sarah Johnson', 'Library Technician', 6000, 'sjohnsonlib@gmail.com', 7653456782)")
        myc.execute("INSERT INTO Employee VALUES (445566, 'Michael456', 'Michael Brown', 'Library Assistant', 5500, 'michaelbrown@gmail.com', 6544567893)")
        myc.execute("INSERT INTO Employee VALUES (556677, 'Laura@books', 'Laura Lee', 'Archivist', 8000, 'lauralee.archives@gmail.com', 5435678904)")
        myc.execute("INSERT INTO Employee VALUES (667788, 'Tom.Library', 'Tom Harris', 'Library Specialist', 7500, 'tomharris.lib@gmail.com', 4326789015)")
        myc.execute("INSERT INTO Employee VALUES (778899, 'Anna.Books', 'Anna White', 'Cataloger', 7200, 'annawhite.books@gmail.com', 3217890126)")
        myc.execute("INSERT INTO Employee VALUES (889900, 'David@lib123', 'David Martin', 'Library Clerk', 7000, 'davidmartin.lib@gmail.com', 2108901237)")
        myc.execute("INSERT INTO Employee VALUES (990011, 'Nancy.Librarian', 'Nancy Scott', 'Library Director', 9000, 'nancyscott.director@gmail.com', 1099012348)")
        mydb.commit()
def search(window):
    window.geometry("1600x900")
    window.title("Search")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    def show(window):
        va97=g.get()
        myc.execute('select * from library where bookno={}'.format(va97))
        er=myc.fetchall()
        r=[]
        total_rows=3
        total_columns=2
        for lk in er:
            for kl in lk:
                r.append(kl)
        hg=[("Book No.",r[0]),("Name",r[1]),("Quantity",r[2])]
        frm_form9 = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
        frm_form9.pack()
        frm_form9.place(x=500,y=232)
        for i0 in range(total_rows):
            for j0 in range(total_columns):
                if j0 ==0:
                    entry10= tk.Label(frm_form9,text=hg[i0][j0], width=20,bg='#DB6854',fg='White',font=('calibri', 15, 'bold'))
                else:
                    entry10 = tk.Label(frm_form9,text=hg[i0][j0], width=40, fg='#DB6854',bg='White',font=('calibri', 15, ''))
                entry10.grid(row=i0, column=j0)
    def chck():
        v=g.get()
        myc.execute('select bookno from library')
        er=myc.fetchall()
        r=[]
        for lk in er:
            for kl in lk:
                r.append(int(kl))
        if v=='':
            pass
        elif int(v) not in r:
            messagebox.showerror("Error","book doesn't Exist")
        else:
            show(window)
    g=tk.Entry(master=window,width=50)
    g.place(x=900,y=165)
    menu(window)
    click=ImageTk.PhotoImage(file="search.jpeg")
    buttons=tk.Button(window,image=click,command=lambda:chck(),relief=tk.FLAT,font=("calibri","20","bold"),fg="white",bg="#DB6854")
    buttons.place(x=1200,y=165)
    window.mainloop()
def mid():
    temp3=True
    while temp3==True:
        list1=['1','2','3','4','5','6','7','8','9','0']
        x=random.choice(list1)
        y=random.choice(list1)
        z=random.choice(list1)
        q=random.choice(list1)
        md=x+y+z+q
        check=[]
        if md in check:
            continue
        else:
            check=check+[md]
            temp3=False
    return(md)
def membership(window):
    def submit():
        var1=e1.get()
        var2=e2.get()
        var3=e3.get()
        var4=mid()
        var5=datetime.now().time()
        var6=var5.strftime('%H:%M:%S')
        myc.execute("Select Name from member")
        gj=[]
        lk2=myc.fetchall()
        for hj in lk2:
            for jh in hj:
                gj.append(jh)
        if var1=='' or var2=='' or var3=='':
            messagebox.showerror("Error","ALL THE FIELDS ARE REQUIRED")
        else:
            var1=var1.lower()
            if var1 in gj:
                messagebox.showerror("Error","Memeber Already Exisits ")
            else:
                var2=int(var2)
                myc.execute("INSERT INTO member VALUES({},'{}',{},'{}','{}')".format(var4,var1,var2,var6,var3))
                mydb.commit()
                messagebox.showinfo("Success","Member Added Successfully")
                Home(window)
                
    window.geometry("1600x900")
    window.title("Membership")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    frm_form9 = tk.Frame(bg="White",relief=tk.FLAT, borderwidth=0)
    frm_form9.pack()
    frm_form9.place(x=500,y=232)
    l1=tk.Label(frm_form9,text='Name',bg='white',fg='#DB6854')
    l1.config(font=("calibri","20","bold"))
    l1.grid(row=0,column=0)
    e1=tk.Entry(frm_form9,width=25,border=1)
    e1.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e1.grid(row=0,column=1)
    l2=tk.Label(frm_form9,text='Age',bg='white',fg='#DB6854')
    l2.config(font=("calibri","20","bold"))
    l2.grid(row=1,column=0)
    e2=tk.Entry(frm_form9,width=25,border=1)
    e2.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e2.grid(row=1,column=1)
    l3=tk.Label(frm_form9,text='Type\n of membership',bg='white',fg='#DB6854')
    l3.config(font=("calibri","20","bold"))
    l3.grid(row=2,column=0)
    e3=tk.Entry(frm_form9,width=25,border=1)
    e3.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e3.grid(row=2,column=1)
    button2=tk.Button(window,text="SUBMIT",command=lambda:submit(),font=("calibri","15","bold"),fg="white",bg="#DB6854")
    button2.place(x=650,y=380)
    window.mainloop()  
def remove(window):
    def submit():
        var1=e1.get()
        myc.execute("Select bookno from library")
        gj=[]
        lk2=myc.fetchall()
        for hj in lk2:
            for jh in hj:
                gj.append(jh)
        if var1=='':
            messagebox.showerror("Error","ALL THE FIELDS ARE REQUIRED")
        else:
            try:
                var1=int(var1)
                if var1 not in gj:
                    messagebox.showerror("Error","Book Doesn't Exisit")
                else:
                    myc.execute("Delete from library where bookno={}".format(var1))
                    mydb.commit()
                    messagebox.showinfo("Success","Book Removed Successfully")
                    Home(window)
            except:
                mydb.rollback()
                messagebox.showerror("Error","Only Integers allowed")
    window.geometry("1600x900")
    window.title("Remove")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    frm_form9 = tk.Frame(bg="White",relief=tk.FLAT, borderwidth=0)
    frm_form9.pack()
    frm_form9.place(x=500,y=232)
    l1=tk.Label(frm_form9,text='Book ID.',bg='white',fg='#DB6854')
    l1.config(font=("calibri","20","bold"))
    l1.grid(row=0,column=0)
    e1=tk.Entry(frm_form9,width=25,border=1)
    e1.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e1.grid(row=0,column=1)
    button2=tk.Button(window,text="SUBMIT",command=lambda:submit(),font=("calibri","15","bold"),fg="white",bg="#DB6854")
    button2.place(x=650,y=380)
    window.mainloop()
def update(window):
    def submit():
        var1=e1.get()
        var2=e2.get()
        myc.execute("Select bookno from library")
        gj=[]
        lk2=myc.fetchall()
        for hj in lk2:
            for jh in hj:
                gj.append(jh)
        if var1=='' or var2=='':
            messagebox.showerror("Error","ALL THE FIELDS ARE REQUIRED")
        else:
            try:
                var1=int(var1)
                var2=int(var2)
                if var1 not in gj:
                    messagebox.showerror("Error","book Doesn't Exisit")

                else:
                    myc.execute("Update library set quantity={} where bookNo={}".format(var2,var1))
                    mydb.commit()
                    messagebox.showinfo("Success","Book Updated Successfully")
                    Home(window)
            except:
                mydb.rollback()
                messagebox.showerror("Error","Only Integers allowed")
    window.geometry("1600x900")
    window.title("Update")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    frm_form9 = tk.Frame(bg="White",relief=tk.FLAT, borderwidth=0)
    frm_form9.pack()
    frm_form9.place(x=500,y=232)
    l1=tk.Label(frm_form9,text='Book ID.',bg='white',fg='#DB6854')
    l1.config(font=("calibri","20","bold"))
    l1.grid(row=0,column=0)
    e1=tk.Entry(frm_form9,width=25,border=1)
    e1.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e1.grid(row=0,column=1)
    e2=tk.Entry(frm_form9,width=25,border=1)
    e2.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e2.grid(row=1,column=1)
    l3=tk.Label(frm_form9,text='Quantity',bg='white',fg='#DB6854',font=("calibri","20","bold"))
    l3.grid(row=1,column=0)
    button2=tk.Button(window,text="SUBMIT",command=lambda:submit(),font=("calibri","15","bold"),fg="white",bg="#DB6854")
    button2.place(x=650,y=380)
    window.mainloop()
def add(window):
    def submit():
        var1=e1.get()
        var2=e2.get()
        var3=e3.get()
        myc.execute("Select Name from library")
        gj=[]
        lk2=myc.fetchall()
        for hj in lk2:
            for jh in hj:
                gj.append(jh)
        myc.execute("Select Quantity from library")
        jk=[]
        lk=myc.fetchall()
        for hj in lk:
            for jh in hj:
                jk.append(jh)
        var7 = sum(jk)
        if var1=='' or var2=='' or var3=='':
            messagebox.showerror("Error","ALL THE FIELDS ARE REQUIRED")
        else:
            var2=var2.lower()
            if var2 in gj:
                messagebox.showerror("Error","Book Already Exisits so please update the quantity if needed")
            else:
                var1=int(var1)
                var3=int(var3)
                myc.execute("INSERT INTO library VALUES({},'{}',{})".format(var1,var2,var3))
                mydb.commit()
                messagebox.showinfo("Success","Book Added Successfully")
                Home(window)
    window.geometry("1600x900")
    window.title("Add")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    frm_form9 = tk.Frame(bg="White",relief=tk.FLAT, borderwidth=0)
    frm_form9.pack()
    frm_form9.place(x=500,y=232)
    l1=tk.Label(frm_form9,text='Book ID.',bg='white',fg='#DB6854')
    l1.config(font=("calibri","20","bold"))
    l1.grid(row=0,column=0)
    e1=tk.Entry(frm_form9,width=25,border=1)
    e1.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e1.grid(row=0,column=1)
    e2=tk.Entry(frm_form9,width=25,border=1)
    e2.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e2.grid(row=1,column=1)
    l2=tk.Label(frm_form9,text='Book Name',bg='white',fg='#DB6854',font=("calibri","20","bold"))
    l2.grid(row=1,column=0)
    l3=tk.Label(frm_form9,text='Quantity',bg='white',fg='#DB6854',font=("calibri","20","bold"))
    l3.grid(row=2,column=0)
    e3=tk.Entry(frm_form9,width=25,border=1)
    e3.config(font=("calibri","15","bold"),bg='white',fg='#DB6854')
    e3.grid(row=2,column=1)
    button2=tk.Button(window,text="SUBMIT",command=lambda:submit(),font=("calibri","15","bold"),fg="white",bg="#DB6854")
    button2.place(x=650,y=380)
    window.mainloop()
def menu(window):
    def logout(window):
        try:
            myc.execute("truncate table login")
            mydb.commit()
            login(window)
        except:
            mydb.rollback()
    button6=tk.Button(window,text="Add book",command=lambda:add(window),relief=tk.FLAT,font=("calibri","20","bold"),fg="white",bg="#DB6854")
    button6.place(x=85,y=200)
    button6=tk.Button(window,text=" Update book",command=lambda:update(window),relief=tk.FLAT,font=("calibri","20","bold"),fg="white",bg="#DB6854")
    button6.place(x=75,y=270)
    button6=tk.Button(window,text=" Remove book",command=lambda:remove(window),relief=tk.FLAT,font=("calibri","20","bold"),fg="white",bg="#DB6854")
    button6.place(x=75,y=340)
    button6=tk.Button(window,text="Membership",command=lambda:membership(window),relief=tk.FLAT,font=("calibri","20","bold"),fg="white",bg="#DB6854")
    button6.place(x=90,y=410)
    button7=tk.Button(window,text="Search",command=lambda:search(window),relief=tk.FLAT,font=("calibri","20","bold"),fg="white",bg="#DB6854")
    button7.place(x=90,y=480)
    button6=tk.Button(window,text="Logout",command=lambda:logout(window),font=("calibri","15","bold"),fg="#DB6854",bg="white")
    button6.place(x=100,y=600,width=70,height=30)
def Home(window):
    window.geometry("1600x900")
    window.title("Page")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    window.mainloop()
def login(window):
    def submit(window):
        g67=e1.get()
        f67=e2.get()
        myc.execute("Select empno from employee")
        k67=myc.fetchall()
        r67=[]
        for i67 in k67:
            for j67 in i67:
                r67.append(j67)
        if g67=='' or f67=='':
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                g68=int(g67)
                if (g68 not in r67):
                    messagebox.showerror("Error","Empno doesn't Exist")
                elif (g68 in r67):
                        myc.execute("Select password from employee where empno={}".format(g68))
                        k68=myc.fetchone()
                        va68=''
                        for i68 in k68:
                            va68=va68+i68
                        if f67!=va68:
                            messagebox.showerror("Error","Incorrect Password")
                        else:
                           myc.execute("Select name from employee where empno={}".format(g68))
                           k69=myc.fetchone()
                           va69=''
                           for i69 in k69:
                               va69=va69+i69
                           try:
                               myc.execute("INSERT INTO login values({},'{}','{}')".format(g68,f67,va69))
                               messagebox.showinfo("Login","Login Succesful")
                               mydb.commit()
                               Home(window)
                           except:
                               mydb.rollback()
                               messagebox.showerror("Error","Login Unsuccessful")
            except:
                messagebox.showerror("Error","Empno should be an integer")
    def show():
        if(c_v1.get()==1):
            e2.config(show='')
        else:
            e2.config(show='*') 

    def chome4():
        main(window)      
    window.geometry('1600x900')
    window.title('LOGIN')
    bg=ImageTk.PhotoImage(file="login.png")
    bglb=tk.Label(window,image=bg)
    bglb.place(x=-50,y=-50,width=1600,height=900)
    l3=tk.Label(window,text='Staff',bg='#DB6854',fg='white',width=10)
    l3.config(font=("calibri","60","bold"))
    l3.place(x=390,y=150)
    l1=tk.Label(window,text='Emp No.',bg='#DB6854',fg='white')
    l1.config(font=("calibri","20","bold"))
    l1.place(x=400,y=300)
    e1=tk.Entry(window,width=25,border=1)
    e1.config(font=("calibri","15","bold"),bg='#DB6854',fg='white')
    e1.place(x=525,y=305)
    e2=tk.Entry(window,width=25,border=1,show='*')
    e2.config(font=("calibri","15","bold"),bg='#DB6854',fg='white')
    e2.place(x=525,y=350)
    l2=tk.Label(window,text='Password',bg='#DB6854',fg='white',font=("calibri","20","bold"))
    l2.place(x=400,y=350)
    button3=tk.Button(window,text="Back To Home",relief=tk.FLAT,command=lambda:chome4(),font=("calibri","20","bold"),fg="white",bg="#DB6854")
    button3.place(x=430,y=430)
    button46=tk.Button(window,text="Login",relief=tk.FLAT,command=lambda:submit(window),font=("calibri","20","bold"),fg="white",bg="#DB6854")
    button46.place(x=700,y=430)
    window.mainloop()
def main(window):
    window.title("Home")
    window.geometry("1600x900")
    bg=ImageTk.PhotoImage(file="HOME.png")
    bglb=tk.Label(window,image=bg)
    bglb.place(x=-50,y=-50,width=1600,height=900)
    button=tk.Button(window,text="LOGIN",command=lambda:login(window),relief=tk.FLAT,font=("calibri","28","bold"),fg="white",bg="#DB6854")
    button.place(x=220,y=523)
    window.mainloop()
createdatabase()
createtables()
window=tk.Tk()
main(window)

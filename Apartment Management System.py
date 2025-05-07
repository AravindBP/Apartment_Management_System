from tkinter import *
from tkinter import messagebox
import mysql.connector as MQ
from tkinter import ttk
from random import *
con=MQ.connect(host='localhost',user='root',password='123456',database='grade12')
rd=randint(1,3)
r=Tk()
r.title('Login')
r.geometry('1000x800+100+0')
r.configure(bg='lawn green')
r.resizable(False,False)
rt=()
if rd==1:
    c=Canvas(r,height=1500,width=1500)
    fp=PhotoImage(file="C:\\Users\\aravi\\OneDrive\\Pictures\\HomePageBG.png")
    bl=Label(r,image=fp)
    bl.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
elif rd==2:
    c=Canvas(r,height=1500,width=1500)
    fp=PhotoImage(file="C:\\Users\\aravi\\OneDrive\\Pictures\\HomePageBG2.png")
    bl=Label(r,image=fp)
    bl.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
elif rd==3:
    c=Canvas(r,height=1500,width=1500)
    fp=PhotoImage(file="C:\\Users\\aravi\\OneDrive\\Pictures\\HomePageBG3.png")
    bl=Label(r,image=fp)
    bl.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
img=PhotoImage(file="C:\\Users\\aravi\\OneDrive\\Pictures\\Lake Drive Apartments.png")
p=Label(r,image=img,compound='top').place(x=150,y=20)
def log():
    if (u.get(),p.get())==('Aravind','IchigoGOD878') or (u.get(),p.get())==('Satvik','Asta#911') or (u.get(),p.get())==('Gambhir','LuffyKaizoku@272'):
        messagebox.showinfo(title='Login',message='Logged in successfully')
        r.destroy()
        import Supporter
    else:
        messagebox.showerror(title='Error',message='Wrong Username/Password')
def out():
    r.destroy()
un=Label(r,text='Username:',fg='deep sky blue',bg='black',font=('Times New Roman',18))
pw=Label(r,text='Password:',fg='deep sky blue',bg='black',font=('Times New Roman',18))
u=StringVar()
p=StringVar()
unp=Entry(r,textvariable=u,width=50)
pwp=Entry(r,textvariable=p,width=50)
un.place(x=320,y=400)
pw.place(x=323,y=480)
unp.place(x=320,y=440)
pwp.place(x=320,y=520)
b=Button(r,text='Enter',fg='lawn green',bg='black',command=log,font=('Times New Roman',12))
b1=Button(r,text='Cancel',fg='lawn green',bg='black',command=out,font=('Times New Roman',12))
b.place(x=320,y=560)
b1.place(x=390,y=560)
r.mainloop()

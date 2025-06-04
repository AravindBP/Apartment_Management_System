from tkinter import *
from tkinter import messagebox
import mysql.connector as MQ
from tkinter import ttk
from random import *
def adp():
    def out1():
        atr.destroy()
    def inst():
        v=(Fne.get(),SQe.get(),BDe.get(),FLe.get(),PRe.get(),Ave.get(),RNe.get(),RDe.get())
        x=0
        if 0 in v or '' in v:
            messagebox.showerror(title='Error',message='Invalid Values Entered')
        cur.execute("Select * from flat")
        r=cur.fetchall()
        for i in r:
            if Fne.get()==i[0]:
                x=1
                break
        if x==1:
            messagebox.showerror(title='Error',message='The Apartment already exists')
        else:
            q="Insert Into Flat Values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(q,v)
            con.commit()
            atr.destroy()
    atr=Tk()
    atr.configure(bg='cyan')
    atr.title('Add Apartment')
    atr.geometry('500x500+50+100')
    atr.resizable(False,False)
    L=Label(atr,text='Add Apartments',fg='magenta2',bg='black',font=('Times New Roman',24))
    Fn=Label(atr,text='Fno',fg='snow',bg='black',font=('Times New Roman',12))
    SQ=Label(atr,text='SqFt',fg='snow',bg='black',font=('Times New Roman',12))
    BD=Label(atr,text='Bed_Num',fg='snow',bg='black',font=('Times New Roman',12))
    FL=Label(atr,text='Floor',fg='snow',bg='black',font=('Times New Roman',12))
    PR=Label(atr,text='Price',fg='snow',bg='black',font=('Times New Roman',12))
    Av=Label(atr,text='Available',fg='snow',bg='black',font=('Times New Roman',12))
    RN=Label(atr,text='Reg_Num',fg='snow',bg='black',font=('Times New Roman',12))
    RD=Label(atr,text='Reg_Date',fg='snow',bg='black',font=('Times New Roman',12))
    Fne=Entry(atr,width=30)
    SQe=Entry(atr,width=30)
    BDe=Entry(atr,width=30)
    FLe=Entry(atr,width=30)
    PRe=Entry(atr,width=30)
    Ave=Entry(atr,width=30)
    RNe=Entry(atr,width=30)
    RDe=Entry(atr,width=30)
    L.place(x=140,y=40)
    Fn.place(x=60,y=110)
    SQ.place(x=55,y=140)
    BD.place(x=25,y=170)
    FL.place(x=55,y=200)
    PR.place(x=55,y=230)
    Av.place(x=35,y=260)
    RN.place(x=30,y=290)
    RD.place(x=30,y=320)
    Fne.place(x=100,y=110)
    SQe.place(x=100,y=140)
    BDe.place(x=100,y=170)
    FLe.place(x=100,y=200)
    PRe.place(x=100,y=230)
    Ave.place(x=100,y=260)
    RNe.place(x=100,y=290)
    RDe.place(x=100,y=320)
    eb=Button(atr,text='Enter',fg='DodgerBlue2',bg='black',command=inst,font=('Times New Roman',12))
    cb=Button(atr,text='Cancel',fg='DodgerBlue2',bg='black',command=out1,font=('Times New Roman',12))
    eb.place(x=60,y=380)
    cb.place(x=150,y=380)
def delp():
    def out2():
        dlp.destroy()
    def Del():
        v=(e.get(),) 
        Q="Select * from Flat"
        cur.execute(Q)
        r=cur.fetchall()
        x=0
        for i in r:
            if e.get()==i[0]:
                x+=1
        if x==0:
            messagebox.showerror(title='Error',message='No such Apartment exists in Database')
        else:
            q="Delete from Flat where Fno=%s "
            cur.execute(q,v)
            con.commit()
            dlp.destroy()
    dlp=Tk()
    dlp.configure(bg='green1')
    dlp.geometry('300x300+50+0')
    dlp.title('Delete Apartments')
    Lb=Label(dlp,text='Deleting Apartment',fg='lavender',bg='black',font=('Times New Roman',20))
    L=Label(dlp,text='Fno to Delete',fg='snow',bg='black',font=('Times New Roman',14))
    Lb.place(x=40,y=50)
    L.place(x=40,y=130)
    e=Entry(dlp,width=30)
    e.place(x=40,y=160)
    b=Button(dlp,text='Delete',fg='deep sky blue',bg='black',command=Del,font=('Times New Roman',12))
    b.place(x=40,y=200)
    b1=Button(dlp,text='Cancel',fg='deep sky blue',bg='black',command=out2,font=('Times New Roman',12))
    b1.place(x=120,y=200)
def mdp():
    def udm():
        def udc():
            mx.destroy()
        def upd():
            Q="Select * from Flat"
            cur.execute(Q)
            r=cur.fetchall()
            x=0
            for i in r:
                if fe.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Apartment exists in Database')
            else:
                v=(de.get(),fe.get())
                Q="Update Flat set SqFt=%s where Fno=%s"
                cur.execute(Q,v)
                con.commit()
                mx.destroy()
        mx=Tk()
        mx.title('Modify Dimension')
        mx.configure(bg='magenta2')
        mx.geometry('400x300')
        mx.resizable(False,False)
        L=Label(mx,text='Modify Dimensions',fg='green2',bg='black',font=('Times New Roman',24)).place(x=80,y=40)
        f=Label(mx,text='Fno',fg='snow',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        d=Label(mx,text='SqFt',fg='snow',bg='black',font=('Times New Roman',14)).place(x=27,y=160)
        fe=Entry(mx,width=30)
        de=Entry(mx,width=30)
        fe.place(x=80,y=120)
        de.place(x=80,y=160)
        h=Button(mx,text='Enter',fg='DodgerBlue2',bg='black',command=upd,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(mx,text='Cancel',fg='DodgerBlue2',bg='black',command=udc,font=('Times New Roman',14)).place(x=110,y=200)
    def ubm():
        def ubc():
            hx.destroy()
        def upb():
            Q="Select * from Flat"
            cur.execute(Q)
            r=cur.fetchall()
            x=0
            for i in r:
                if fe.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Apartment exists in Database')
            else:
                v=(be.get(),fe.get())
                Q="Update Flat set Bed_Num=%s where Fno=%s"
                cur.execute(Q,v)
                con.commit()
                hx.destroy()
        hx=Tk()
        hx.configure(bg='green2')
        hx.geometry('400x300')
        hx.title('Modify Bedrooms')
        hx.resizable(False,False)
        L=Label(hx,text='Modify Bedrooms',fg='snow',bg='black',font=('Times New Roman',24)).place(x=80,y=40)
        f=Label(hx,text='Fno',fg='snow',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        d=Label(hx,text='Bed_Num',fg='snow',bg='black',font=('Times New Roman',14)).place(x=10,y=160)
        fe=Entry(hx,width=30)
        be=Entry(hx,width=30)
        fe.place(x=80,y=120)
        be.place(x=110,y=160)
        h=Button(hx,text='Enter',fg='DodgerBlue2',bg='black',command=upb,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(hx,text='Cancel',fg='DodgerBlue2',bg='black',command=ubc,font=('Times New Roman',14)).place(x=110,y=200)
    def ufm():
        def ulc():
            fx.destroy()
        def upl():
            Q="Select * from Flat"
            cur.execute(Q)
            r=cur.fetchall()
            x=0
            for i in r:
                if fe.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Apartment exists in Database')
            else:
                v=(le.get(),fe.get())
                Q="Update Flat set Floor=%s where Fno=%s"
                cur.execute(Q,v)
                con.commit()
                fx.destroy()
        fx=Tk()
        fx.configure(bg='green2')
        fx.geometry('400x300')
        fx.title('Modify Floor')
        fx.resizable(False,False)
        L=Label(fx,text='Modify Floor',fg='turquoise1',bg='black',font=('Times New Roman',24)).place(x=80,y=40)
        f=Label(fx,text='Fno',fg='turquoise1',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        d=Label(fx,text='Floor',fg='turquoise1',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        fe=Entry(fx,width=30)
        le=Entry(fx,width=30)
        fe.place(x=80,y=120)
        le.place(x=80,y=160)
        h=Button(fx,text='Enter',fg='lawn green',bg='black',command=upl,font=('Times New Roman',14)).place(x=25,y=200)
        m=Button(fx,text='Cancel',fg='lawn green',bg='black',command=ulc,font=('Times New Roman',14)).place(x=110,y=200)
    def upm():
        def upc():
            px.destroy()
        def upp():
            Q="Select * from Flat"
            cur.execute(Q)
            r=cur.fetchall()
            x=0
            for i in r:
                if fe.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Apartment exists in Database')
            else:
                v=(pe.get(),fe.get())
                Q="Update Flat set Price=%s where Fno=%s"
                cur.execute(Q,v)
                con.commit()
                px.destroy()
        px=Tk()
        px.configure(bg='cyan2')
        px.geometry('400x300')
        px.title('Modify Price')
        px.resizable(False,False)
        L=Label(px,text='Modify price',fg='snow',bg='black',font=('Times New Roman',24)).place(x=80,y=40)
        f=Label(px,text='Fno',fg='snow',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        d=Label(px,text='Floor',fg='snow',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        fe=Entry(px,width=30)
        pe=Entry(px,width=30)
        fe.place(x=80,y=120)
        pe.place(x=80,y=160)
        h=Button(px,text='Enter',fg='lawn green',bg='black',command=upp,font=('Times New Roman',14)).place(x=25,y=200)
        m=Button(px,text='Cancel',fg='lawn green',bg='black',command=upc,font=('Times New Roman',14)).place(x=110,y=200)
    def upa():
        def uac():
            ux.destroy()
        def upm():
            Q="Select * from Flat"
            cur.execute(Q)
            r=cur.fetchall()
            x=0
            for i in r:
                if fe.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Apartment exists in Database')
            else:
                v=(ae.get(),fe.get())
                Q="Update Flat set Available=%s where Fno=%s"
                cur.execute(Q,v)
                con.commit()
                ux.destroy()
        ux=Tk()
        ux.configure(bg='green2')
        ux.geometry('400x300')
        ux.title('Modify Availability')
        ux.resizable(False,False)
        L=Label(ux,text='Modify Availability',fg='red',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        f=Label(ux,text='Fno',fg='red',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        d=Label(ux,text='Available',fg='red',bg='black',font=('Times New Roman',14)).place(x=10,y=160)
        fe=Entry(ux,width=30)
        ae=Entry(ux,width=30)
        fe.place(x=80,y=120)
        ae.place(x=110,y=160)
        h=Button(ux,text='Enter',fg='DodgerBlue2',bg='black',command=upm,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(ux,text='Cancel',fg='DodgerBlue2',bg='black',command=uac,font=('Times New Roman',14)).place(x=110,y=200)
    def urn():
        def urc():
            un.destroy()
        def urm():
            Q="Select * from Flat"
            cur.execute(Q)
            r=cur.fetchall()
            x=0
            for i in r:
                if fe.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Apartment exists in Database')
            else:
                v=(re.get(),fe.get())
                Q="Update Flat set Reg_Num=%s where Fno=%s"
                cur.execute(Q,v)
                con.commit()
                un.destroy()
        un=Tk()
        un.configure(bg='magenta2')
        un.geometry('400x300')
        un.title('Modify Registration Number')
        un.resizable(False,False)
        L=Label(un,text='Modify Reg_Num',fg='green yellow',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        f=Label(un,text='Fno',fg='green yellow',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        r=Label(un,text='Reg_Num',fg='green yellow',bg='black',font=('Times New Roman',14)).place(x=10,y=160)
        fe=Entry(un,width=30)
        re=Entry(un,width=30)
        fe.place(x=80,y=120)
        re.place(x=110,y=160)
        h=Button(un,text='Enter',fg='DodgerBlue2',bg='black',command=urm,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(un,text='Cancel',fg='DodgerBlue2',bg='black',command=urc,font=('Times New Roman',14)).place(x=110,y=200)
    def udn():
        def urx():
            um.destroy()
        def udk():
            Q="Select * from Flat"
            cur.execute(Q)
            r=cur.fetchall()
            x=0
            for i in r:
                if fe.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Apartment exists in Database')
            else:
                v=(rk.get(),fe.get())
                Q="Update Flat set Reg_Date=%s where Fno=%s"
                cur.execute(Q,v)
                con.commit()
                um.destroy()
        um=Tk()
        um.configure(bg='blue2')
        um.geometry('400x300')
        um.title('Modify Registration Date')
        um.resizable(False,False)
        L=Label(um,text='Modify Reg_Date',fg='snow',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        f=Label(um,text='Fno',fg='snow',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        r=Label(um,text='Reg_Num',fg='snow',bg='black',font=('Times New Roman',14)).place(x=10,y=160)
        fe=Entry(um,width=30)
        rk=Entry(um,width=30)
        fe.place(x=80,y=120)
        rk.place(x=110,y=160)
        h=Button(um,text='Enter',fg='green yellow',bg='black',command=udk,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(um,text='Cancel',fg='green yellow',bg='black',command=urx,font=('Times New Roman',14)).place(x=110,y=200)
    def xt():
        mox.destroy()
    mox=Tk()
    mox.title("Modify Apartment")
    mox.configure(bg='deep sky blue')
    mox.geometry('400x500+0+100')
    mox.resizable(False,False)
    LL=Label(mox,text='Modify Apartment Details',fg='turquoise2',bg='black',font=('Times New Roman',20)).place(x=60,y=40)
    ud=Button(mox,text='Update Dimension',fg='green2',bg='black',command=udm,font=('Times New Roman',14)).place(x=50,y=120)
    ub=Button(mox,text='Update Bed_Num',fg='green2',bg='black',command=ubm,font=('Times New Roman',14)).place(x=50,y=160)
    uf=Button(mox,text='Update Floor',fg='green2',bg='black',command=ufm,font=('Times New Roman',14)).place(x=50,y=200)
    up=Button(mox,text='Update Price',fg='green2',bg='black',command=upm,font=('Times New Roman',14)).place(x=50,y=240)
    ua=Button(mox,text='Update Availability',fg='green2',bg='black',command=upa,font=('Times New Roman',14)).place(x=50,y=280)
    rn=Button(mox,text='Update Reg_Num',fg='green2',bg='black',command=urn,font=('Times New Roman',14)).place(x=50,y=320)
    kd=Button(mox,text='Update Reg_Date',fg='green2',bg='black',command=udn,font=('Times New Roman',14)).place(x=50,y=360)
    tr=Button(mox,text='Exit',fg='green2',bg='black',command=xt,font=('Times New Roman',14)).place(x=50,y=400)
def mdo():
    def xt():
        mod.destroy()
    def xon():
        def ttr():
            n.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                v=(ne.get(),ie.get())
                q="Update Owner set Owner_Name=%s where Owner_Id=%s"
                cur.execute(q,v)
                con.commit()
                n.destroy()
        n=Tk()
        n.title('Modify Owner Name')
        n.configure(bg='DodgerBlue2')
        n.geometry('400x300')
        n.resizable(False,False)
        L=Label(n,text='Modify Owner_Name',fg='snow',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(n,text='Owner_Id',fg='snow',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(n,text='Owner_Name',fg='snow',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        ie=Entry(n,width=30)
        ne=Entry(n,width=30)
        ie.place(x=130,y=120)
        ne.place(x=140,y=160)
        h=Button(n,text='Enter',fg='green yellow',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(n,text='Cancel',fg='green yellow',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    def xom():
        def ttr():
            mn.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                q="Update Owner set Owner_Mobile=%s where Owner_Id=%s"
                v=(me.get(),ie.get())
                cur.execute(q,v)
                con.commit()
                mn.destroy()
        mn=Tk()
        mn.title("Modify Owner's Mobile")
        mn.configure(bg='cyan')
        mn.geometry('400x300')
        mn.resizable(False,False)
        L=Label(mn,text="Modify Owner's Mobile",fg='magenta2',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(mn,text='Owner_Id',fg='magenta2',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(mn,text='Owner_Mobile',fg='magenta2',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        ie=Entry(mn,width=30)
        me=Entry(mn,width=30)
        ie.place(x=130,y=120)
        me.place(x=150,y=160)
        h=Button(mn,text='Enter',fg='green yellow',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(mn,text='Cancel',fg='green yellow',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    def xoi():
        def ttr():
            ni.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                q="Update Owner set Owner_Mail=%s where Owner_Id=%s"
                v=(ae.get(),ie.get())
                cur.execute(q,v)
                con.commit()
                ni.destroy()
        ni=Tk()
        ni.title('Modify Owner Name')
        ni.configure(bg='DodgerBlue2')
        ni.geometry('400x300')
        ni.resizable(False,False)
        L=Label(ni,text='Modify Owner_Mail',fg='red',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(ni,text='Owner_Id',fg='red',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(ni,text='Owner_Mail',fg='red',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        ie=Entry(ni,width=30)
        ae=Entry(ni,width=30)
        ie.place(x=130,y=120)
        ae.place(x=140,y=160)
        h=Button(ni,text='Enter',fg='magenta2',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(ni,text='Cancel',fg='magenta2',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    def xof():
        def ttr():
            fn.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                q="Update Owner set Fno=%s where Owner_Id=%s"
                v=(fe.get(),ie.get())
                cur.execute(q,v)
                con.commit()
                fn.destroy()
        fn=Tk()
        fn.title('Modify Owner Name')
        fn.configure(bg='DodgerBlue2')
        fn.geometry('400x300')
        fn.resizable(False,False)
        L=Label(fn,text='Modify Flat No.',fg='cyan',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(fn,text='Owner_Id',fg='cyan',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(fn,text='Fno',fg='cyan',bg='black',font=('Times New Roman',14)).place(x=30,y=160)
        ie=Entry(fn,width=30)
        fe=Entry(fn,width=30)
        ie.place(x=130,y=120)
        fe.place(x=90,y=160)
        h=Button(fn,text='Enter',fg='green yellow',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(fn,text='Cancel',fg='green yellow',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    mod=Tk()
    mod.title("Modify Owner Details")
    mod.configure(bg='green yellow')
    mod.geometry('400x400+0+100')
    mod.resizable(False,False)
    LL=Label(mod,text='Modify Owner Details',fg='turquoise2',bg='black',font=('Times New Roman',20)).place(x=60,y=40)
    on=Button(mod,text='Update Owner_Name',fg='snow',bg='black',command=xon,font=('Times New Roman',14)).place(x=50,y=120)
    om=Button(mod,text='Update Owner_Mobile',fg='snow',bg='black',command=xom,font=('Times New Roman',14)).place(x=50,y=160)
    ol=Button(mod,text='Update Owner_Mail',fg='snow',bg='black',command=xoi,font=('Times New Roman',14)).place(x=50,y=200)
    fn=Button(mod,text='Update Fno',fg='snow',bg='black',command=xof,font=('Times New Roman',14)).place(x=50,y=240)
    tr=Button(mod,text='Exit',fg='snow',bg='black',command=xt,font=('Times New Roman',14)).place(x=50,y=280)
def dod():
    def otr():
        dox.destroy()
    dox=Tk()
    dox.resizable(False,False)
    dox.configure(bg='deep sky blue')
    dox.geometry('500x300+0+100')
    dox.title('Owner Details')
    cur.execute("Select * from Owner")
    r=cur.fetchall()
    tree=ttk.Treeview(dox)
    tree['show']='headings'
    tree['columns']=('Owner_Id','Owner_Name','Owner_Mobile','Owner_Mail','Fno')
    tree.column('Owner_Id',width=150,minwidth=150,anchor=CENTER)
    tree.column('Owner_Name',width=150,minwidth=150,anchor=CENTER)
    tree.column('Owner_Mobile',width=150,minwidth=150,anchor=CENTER)
    tree.column('Owner_Mail',width=200,minwidth=200,anchor=CENTER)
    tree.column('Fno',width=150,minwidth=150,anchor=CENTER)
    #Inserting the headings
    tree.heading('Owner_Id',text='Owner_Id',anchor=CENTER)
    tree.heading('Owner_Name',text='Owner_Name',anchor=CENTER)
    tree.heading('Owner_Mobile',text='Owner_Mobile',anchor=CENTER)
    tree.heading('Owner_Mail',text='Owner_Mail',anchor=CENTER)
    tree.heading('Fno',text='Fno',anchor=CENTER)
    #Inserting the values
    j=0
    for i in r:
        tree.insert('',j,text="",values=(i[0],i[1],i[2],i[3],i[4]))
        j+=1
    tree.pack()
    #Horizontal ScrollBar
    hsb=ttk.Scrollbar(dox,orient='horizontal')
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    tree.pack()
    #Vertical ScrollBar
    vsb=ttk.Scrollbar(dox,orient='vertical')
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    tree.pack()
    B=Button(dox,text='Exit',fg='snow',bg='black',command=otr,font=("Times New Roman",12)).place(x=340,y=240)
def dva():
    def odx():
        dvx.destroy()
    dvx=Tk()
    dvx.resizable(False,False)
    dvx.title('Available Apartments')
    dvx.geometry('500x300+0+100')
    dvx.configure(bg='yellow2')
    cur.execute("Select * from Flat where Available='Yes'")
    r=cur.fetchall()
    tree=ttk.Treeview(dvx)
    tree['show']='headings'
    tree['columns']=('Fno','SqFt','Bed_Num','Floor','Price','Available','Reg_Num','Reg_Date')
    tree.column("Fno",width=80,minwidth=80,anchor=CENTER)
    tree.column("SqFt",width=80,minwidth=80,anchor=CENTER)
    tree.column("Bed_Num",width=80,minwidth=80,anchor=CENTER)
    tree.column("Floor",width=80,minwidth=80,anchor=CENTER)
    tree.column("Price",width=80,minwidth=80,anchor=CENTER)
    tree.column("Available",width=80,minwidth=80,anchor=CENTER)
    tree.column("Reg_Num",width=80,minwidth=80,anchor=CENTER)
    tree.column("Reg_Date",width=80,minwidth=80,anchor=CENTER)
    #Creating Heading for a given column
    tree.heading('Fno',text='Fno',anchor=CENTER)
    tree.heading('SqFt',text='SqFt',anchor=CENTER)
    tree.heading('Bed_Num',text='Bed_Num',anchor=CENTER)
    tree.heading('Floor',text='Floor',anchor=CENTER)
    tree.heading('Price',text='Price',anchor=CENTER)
    tree.heading('Available',text='Available',anchor=CENTER)
    tree.heading('Reg_Num',text='Reg_Num',anchor=CENTER)
    tree.heading('Reg_Date',text='Reg_Date',anchor=CENTER)
    #Inserting Values into the Tree
    j=0
    for i in r:
        tree.insert('',j,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        j+=1
    tree.pack()
    #Horizontal ScrollBar
    hsb=ttk.Scrollbar(dvx,orient='horizontal')
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    tree.pack()
    #Vertical ScrollBar
    vsb=ttk.Scrollbar(dvx,orient='vertical')
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    tree.pack()
    B=Button(dvx,text='Exit',fg='DodgerBlue2',bg='black',command=odx,font=("Times New Roman",12))
    B.place(x=340,y=240)
def daa():
    def otx():
        aox.destroy()
    aox=Tk()
    aox.resizable(False,False)
    aox.title('All Apartments')
    aox.geometry('500x300+0+100')
    aox.configure(bg='DeepSkyBlue2')
    cur.execute("Select * from Flat")
    r=cur.fetchall()
    tree=ttk.Treeview(aox)
    tree['show']='headings'
    tree['columns']=('Fno','SqFt','Bed_Num','Floor','Price','Available','Reg_Num','Reg_Date')
    tree.column("Fno",width=80,minwidth=80,anchor=CENTER)
    tree.column("SqFt",width=80,minwidth=80,anchor=CENTER)
    tree.column("Bed_Num",width=80,minwidth=80,anchor=CENTER)
    tree.column("Floor",width=80,minwidth=80,anchor=CENTER)
    tree.column("Price",width=80,minwidth=80,anchor=CENTER)
    tree.column("Available",width=80,minwidth=80,anchor=CENTER)
    tree.column("Reg_Num",width=80,minwidth=80,anchor=CENTER)
    tree.column("Reg_Date",width=80,minwidth=80,anchor=CENTER)
    #Creating Heading for a given column
    tree.heading('Fno',text='Fno',anchor=CENTER)
    tree.heading('SqFt',text='SqFt',anchor=CENTER)
    tree.heading('Bed_Num',text='Bed_Num',anchor=CENTER)
    tree.heading('Floor',text='Floor',anchor=CENTER)
    tree.heading('Price',text='Price',anchor=CENTER)
    tree.heading('Available',text='Available',anchor=CENTER)
    tree.heading('Reg_Num',text='Reg_Num',anchor=CENTER)
    tree.heading('Reg_Date',text='Reg_Date',anchor=CENTER)
    #Inserting Values into the Tree
    j=0
    for i in r:
        tree.insert('',j,text="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        j+=1
    tree.pack()
    #Horizontal ScrollBar
    hsb=ttk.Scrollbar(aox,orient='horizontal')
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    tree.pack()
    #Vertical ScrollBar
    vsb=ttk.Scrollbar(aox,orient='vertical')
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    tree.pack()
    B=Button(aox,text='Exit',fg='lawn green',bg='black',command=otx,font=("Times New Roman",12))
    B.place(x=340,y=240)
def aow():
    def out3():
        aox.destroy()
    def aon():
        v=(OWe.get(),ONe.get(),OMe.get(),OAe.get(),FNe.get())
        if '' in v or 0 in v:
            messagebox.showerror(title='Error',message='Empty Values not allowed')
        x=0
        q="select * from Owner"
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            if i[0]==OWe.get():
                x=1
        if x==0:
            Q="Update Flat Set Available='No' where Fno=%s"
            cur.execute(Q,(FNe.get(),))
            con.commit()
        if x==1:
            messagebox.showerror(title='Error',message='Owner already exists in the database')
        else:
            q="Insert into Owner Values(%s,%s,%s,%s,%s)"
            cur.execute(q,v)
            con.commit()
            aox.destroy()
        
    aox=Tk()
    aox.title('Add Owner')
    aox.geometry('500x500+50+100')
    aox.configure(bg='royal blue1')
    aox.resizable(False,False)
    ML=Label(aox,fg='magenta2',bg='black',text='Add Owner',font=('Times New Roman',24))
    OW=Label(aox,fg='steelblue1',bg='black',text='Owner_Id',font=('Times New Roman',14))
    ON=Label(aox,fg='steelblue1',bg='black',text='Owner_Name',font=('Times New Roman',14))
    OM=Label(aox,fg='steelblue1',bg='black',text='Owner_Mobile',font=('Times New Roman',14))
    OA=Label(aox,fg='steelblue1',bg='black',text='Owner_Mail',font=('Times New Roman',14))
    FN=Label(aox,fg='steelblue1',bg='black',text='Fno',font=('Times New Roman',14))
    OWe=Entry(aox,width=30)
    ONe=Entry(aox,width=30)
    OMe=Entry(aox,width=30)
    OAe=Entry(aox,width=30)
    FNe=Entry(aox,width=30)
    eb=Button(aox,fg='steelblue1',bg='black',text='Enter',command=aon,font=('Times New Roman',14))
    cb=Button(aox,fg='steelblue1',bg='black',text='Cancel',command=out3,font=('Times New Roman',14))
    ML.place(x=130,y=50)
    OW.place(x=60,y=180)
    ON.place(x=60,y=230)
    OM.place(x=60,y=280)
    OA.place(x=60,y=330)
    FN.place(x=60,y=380)
    OWe.place(x=165,y=180)
    ONe.place(x=185,y=230)
    OMe.place(x=185,y=280)
    OAe.place(x=175,y=330)
    FNe.place(x=115,y=380)
    eb.place(x=60,y=420)
    cb.place(x=160,y=420)
def deo():
    def out4():
        dex.destroy()
    def dow():
        v=(e.get(),)
        x=0
        Q="Select * from Owner"
        cur.execute(Q)
        r=cur.fetchall()
        for i in r:
            if e.get()==i[0]:
                x+=1
        if x==0:
            messagebox.showerror(title='Error',message='No such Owner exists in Database')
        else:
            q="Delete from Owner Where Owner_Id=%s"
            cur.execute(q,v)
            con.commit()
            dex.destroy()
        if True:
            Q="Update Flat set Available='Yes' where Fno=%s"
            cur.execute(Q,v)
            con.commit()
    dex=Tk()
    dex.geometry('300x300+50+0')
    dex.title('Delete Owner')
    dex.configure(bg='chartreuse2')
    L=Label(dex,text='Deleting Owner',fg='DeepSkyBlue2',bg='black',font=('Times New Roman',20))
    L.place(x=60,y=50)
    D=Label(dex,text='Owner_Id to Delete:',fg='green yellow',bg='black',font=('Times New Roman',14))
    e=Entry(dex,width=30)
    D.place(x=40,y=130)
    e.place(x=40,y=160)
    b=Button(dex,text='Delete',fg='lawn green',bg='black',command=dow,font=('Times New Roman',12))
    b.place(x=40,y=200)
    b1=Button(dex,text='Cancel',fg='lawn green',bg='black',command=out4,font=('Times New Roman',12))
    b1.place(x=120,y=200)
def mdo():
    def xt():
        mod.destroy()
    def xon():
        def ttr():
            n.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                v=(ne.get(),ie.get())
                q="Update Owner set Owner_Name=%s where Owner_Id=%s"
                cur.execute(q,v)
                con.commit()
                n.destroy()
        n=Tk()
        n.title('Modify Owner Name')
        n.configure(bg='DodgerBlue2')
        n.geometry('400x300')
        n.resizable(False,False)
        L=Label(n,text='Modify Owner_Name',fg='snow',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(n,text='Owner_Id',fg='snow',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(n,text='Owner_Name',fg='snow',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        ie=Entry(n,width=30)
        ne=Entry(n,width=30)
        ie.place(x=130,y=120)
        ne.place(x=140,y=160)
        h=Button(n,text='Enter',fg='green yellow',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(n,text='Cancel',fg='green yellow',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    def xom():
        def ttr():
            mn.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                q="Update Owner set Owner_Mobile=%s where Owner_Id=%s"
                v=(me.get(),ie.get())
                cur.execute(q,v)
                con.commit()
                mn.destroy()
        mn=Tk()
        mn.title("Modify Owner's Mobile")
        mn.configure(bg='cyan')
        mn.geometry('400x300')
        mn.resizable(False,False)
        L=Label(mn,text="Modify Owner's Mobile",fg='magenta2',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(mn,text='Owner_Id',fg='magenta2',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(mn,text='Owner_Mobile',fg='magenta2',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        ie=Entry(mn,width=30)
        me=Entry(mn,width=30)
        ie.place(x=130,y=120)
        me.place(x=150,y=160)
        h=Button(mn,text='Enter',fg='green yellow',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(mn,text='Cancel',fg='green yellow',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    def xoi():
        def ttr():
            ni.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                q="Update Owner set Owner_Mail=%s where Owner_Id=%s"
                v=(ae.get(),ie.get())
                cur.execute(q,v)
                con.commit()
                ni.destroy()
        ni=Tk()
        ni.title('Modify Owner Name')
        ni.configure(bg='DodgerBlue2')
        ni.geometry('400x300')
        ni.resizable(False,False)
        L=Label(ni,text='Modify Owner_Mail',fg='red',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(ni,text='Owner_Id',fg='red',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(ni,text='Owner_Mail',fg='red',bg='black',font=('Times New Roman',14)).place(x=25,y=160)
        ie=Entry(ni,width=30)
        ae=Entry(ni,width=30)
        ie.place(x=130,y=120)
        ae.place(x=140,y=160)
        h=Button(ni,text='Enter',fg='magenta2',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(ni,text='Cancel',fg='magenta2',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    def xof():
        def ttr():
            fn.destroy()
        def ttx():
            x=0
            Q="Select * from Owner"
            cur.execute(Q)
            r=cur.fetchall()
            for i in r:
                if ie.get()==i[0]:
                    x+=1
            if x==0:
                messagebox.showerror(title='Error',message='No such Owner exists in Database')
            else:
                q="Update Owner set Fno=%s where Owner_Id=%s"
                v=(fe.get(),ie.get())
                cur.execute(q,v)
                con.commit()
                fn.destroy()
        fn=Tk()
        fn.title('Modify Owner Name')
        fn.configure(bg='DodgerBlue2')
        fn.geometry('400x300')
        fn.resizable(False,False)
        L=Label(fn,text='Modify Flat No.',fg='cyan',bg='black',font=('Times New Roman',24)).place(x=60,y=40)
        oi=Label(fn,text='Owner_Id',fg='cyan',bg='black',font=('Times New Roman',14)).place(x=30,y=120)
        on=Label(fn,text='Fno',fg='cyan',bg='black',font=('Times New Roman',14)).place(x=30,y=160)
        ie=Entry(fn,width=30)
        fe=Entry(fn,width=30)
        ie.place(x=130,y=120)
        fe.place(x=90,y=160)
        h=Button(fn,text='Enter',fg='green yellow',bg='black',command=ttx,font=('Times New Roman',14)).place(x=30,y=200)
        m=Button(fn,text='Cancel',fg='green yellow',bg='black',command=ttr,font=('Times New Roman',14)).place(x=110,y=200)
    mod=Tk()
    mod.title("Modify Owner Details")
    mod.configure(bg='green yellow')
    mod.geometry('400x400+0+100')
    mod.resizable(False,False)
    LL=Label(mod,text='Modify Owner Details',fg='turquoise2',bg='black',font=('Times New Roman',20)).place(x=60,y=40)
    on=Button(mod,text='Update Owner_Name',fg='snow',bg='black',command=xon,font=('Times New Roman',14)).place(x=50,y=120)
    om=Button(mod,text='Update Owner_Mobile',fg='snow',bg='black',command=xom,font=('Times New Roman',14)).place(x=50,y=160)
    ol=Button(mod,text='Update Owner_Mail',fg='snow',bg='black',command=xoi,font=('Times New Roman',14)).place(x=50,y=200)
    fn=Button(mod,text='Update Fno',fg='snow',bg='black',command=xof,font=('Times New Roman',14)).place(x=50,y=240)
    tr=Button(mod,text='Exit',fg='snow',bg='black',command=xt,font=('Times New Roman',14)).place(x=50,y=280)
def at():
    xt=Tk()
    xt.title("Information")
    xt.geometry('450x500')
    xt.resizable(False,False)
    xt.configure(bg='black')
    f=open("About.txt","r")
    t=10
    u=10
    for i in f.readlines():
        LB=Label(xt,text=i,fg='DeepSkyBlue2',bg='black',font=('Times New Roman',14))
        LB.place(x=t,y=u)
        u=u+50
def ot():
    exit()
con=MQ.connect(host='localhost',user='root',password='123456',database='grade12')
cur=con.cursor()
"""q="CREATE TABLE If not exists Flat(Fno Char(4) Primary key,SqFt int Not Null, Bed_Num int,Floor int, Price int,Available Varchar(3),Reg_Num int,Reg_Date Date)"
cur.execute(q)
con.commit()
q="Create Table If not exists Owner(Owner_Id Char(4) Primary Key,Owner_Name Varchar(20), Owner_Mobile Varchar(12),Owner_Mail varchar(30),Fno Char(4) references Flat(Fno))"
cur.execute(q)
con.commit()"""
rt=Tk()
rt.title('Apartment Management System')
rt.geometry('1000x800+100+0')
rt.configure(bg='cyan')
rt.resizable(False,False)
rd=randint(1,3)
if rd==1:
    c=Canvas(rt,height=1500,width=1500)
    fp=PhotoImage(file="MainpageBG2.png")
    bl=Label(rt,image=fp)
    bl.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
elif rd==2:
    c=Canvas(rt,height=1500,width=1500)
    fp=PhotoImage(file="HomePageBG5.png")
    bl=Label(rt,image=fp)
    bl.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
elif rd==3:
    c=Canvas(rt,height=1500,width=1500)
    fp=PhotoImage(file="MainPageBG.png")
    bl=Label(rt,image=fp)
    bl.place(x=0,y=0,relwidth=1,relheight=1)
    c.pack()
img=PhotoImage(file="Lake Drive Apartments.png")
mx=Label(rt,image=img,compound='top')
mx.place(x=150,y=10)
adb=Button(rt,text='Add Apartment',fg='green1',bg='black',command=adp,font=('Times New Roman',14))
mp=Button(rt,text='Modify Apartment',fg='green1',bg='black',command=mdp,font=('Times New Roman',14))
delb=Button(rt,text='Delete Apartment',fg='green1',bg='black',command=delp,font=('Times New Roman',14))
ado=Button(rt,text='Add Owner',fg='green1',bg='black',command=aow,font=('Times New Roman',14))
mow=Button(rt,text='Modify Owner',fg='green1',bg='black',command=mdo,font=('Times New Roman',14))
deo=Button(rt,text='Remove Owner',fg='green1',bg='black',command=deo,font=('Times New Roman',14))
dap=Button(rt,text='Display All Apartment',fg='green1',bg='black',command=daa,font=('Times New Roman',14))
dvp=Button(rt,text='Display Available Apartment',fg='green1',bg='black',command=dva,font=('Times New Roman',14))
dod=Button(rt,text='Display Owner Details',fg='green1',bg='black',command=dod,font=('Times New Roman',14))
ext=Button(rt,text='Logout',fg='green1',bg='black',command=ot,font=('Times New Roman',14))
dxt=Button(rt,text="About",fg='green1',bg='black',command=at,font=('Times New Roman',14))
adb.place(x=50,y=260)
mp.place(x=50,y=310)
delb.place(x=50,y=360)
ado.place(x=50,y=410)
mow.place(x=50,y=460)
deo.place(x=50,y=510)
dap.place(x=50,y=560)
dvp.place(x=50,y=610)
dod.place(x=50,y=660)
ext.place(x=50,y=740)
dxt.place(x=50,y=700)

from tkinter import *
import mainFrame,sqlite3


def registration(root):
    global regframe
    regframe=Frame(root,width=900,height=400,bg='#1d1d1d')
    regframe.pack(side=RIGHT, fill=Y)
    Label(regframe,text='Registration No.',font=('Helvetica',11),bg='#1d1d1d',fg='white').place(x=300,y=20)
    regno=Entry(regframe,font=('Helvetica',11),textvariable=StringVar())
    regno.place(x=450,y=20)


    Label(regframe, text='Student Name', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=55)
    studentname=Entry(regframe, font=('Helvetica', 11), textvariable=StringVar())
    studentname.place(x=450, y=55)


    Label(regframe, text='Father Name', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=90)
    fathername=Entry(regframe, font=('Helvetica', 11), textvariable=StringVar())
    fathername.place(x=450, y=90)


    Label(regframe, text='Hometown', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=125)
    hometown = Entry(regframe, font=('Helvetica', 11), textvariable=StringVar())
    hometown.place(x=450, y=125)


    Label(regframe, text='Mobile No.', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=160)
    mobno = Entry(regframe, font=('Helvetica', 11))
    mobno.place(x=450, y=160)


    #mobno.insert(0,"")
    
    Label(regframe, text='Course', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=195)
    variable = StringVar(regframe)
    variable.set("SSC JEN")
    course = OptionMenu(regframe, variable,'SSC JEN', "PATWAR", "SBI PO", "IBPS PO", "RAILWAY", "INFORMATIC ASSISTANT", "STENO")
    course.config(width="20", bd=2)
    course.place(x=450, y=195)

    # course = Entry(regframe, font=('Helvetica', 11), textvariable=StringVar()).place(x=450, y=195)

    Label(regframe, text='Course Fee', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=234)
    coursefee = Entry(regframe, font=('Helvetica', 11))
    coursefee.place(x=450, y=234)


    Label(regframe, text='Fee Deposit', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=300, y=269)
    feedeposit = Entry(regframe, font=('Helvetica', 11))
    feedeposit.place(x=450, y=269)


    Button(regframe,text='Reset All',font=('Helvetica',11),width=11,command=lambda :resetaction(root)).place(x=300,y=340)
    Button(regframe, text='Back', font=('Helvetica', 11),width=11,command=lambda :backaction(regframe,root)).place(x=400, y=340)
    Button(regframe, text='Submit', font=('Helvetica', 11),width=11,bg='#0d3300',fg='#e0ebeb',command=lambda :submitaction(root,regno,studentname,fathername,hometown,mobno,variable,coursefee,feedeposit)).place(x=505, y=340)

def regframedest():
    if 'regframe' in globals():
        regframe.destroy()
    else:
        pass

def backaction(regframe,root):
    regframedest()
    mainFrame.main(root)
def resetaction(root):
    regframedest()
    registration(root)
def submitaction(root,regno,studentname,fathername,hometown,mobno,variable,coursefee,feedeposit):
    a=regno.get()
    b=studentname.get()
    c=fathername.get()
    d=hometown.get()
    ev=mobno.get()
    e=int(ev)
    f=variable.get()
    gv=coursefee.get()
    g=int(gv)
    hv=feedeposit.get()
    h=int(hv)

    con=sqlite3.connect('PARAMOUNT')
    con.execute('create table if not exists studenttable (Reg_No char[8], Student_Name char[20],Father_Name char[20],Hometown char[10],Mobile_No int[10],Course char[10],Course_Fee int[5],Fee_Deposit int[5],Remaining_Fee int[5])')
    con.commit()
    con.execute("insert into studenttable (Reg_No,Student_Name,Father_Name,Hometown,Mobile_No,Course,Course_Fee,Fee_Deposit,Remaining_Fee) values ('{}','{}','{}','{}',{},'{}',{},{},{})".format(a,b,c,d,e,f,g,h,g-h))
    con.commit()
    con.close()
    regframedest()
    registration(root)

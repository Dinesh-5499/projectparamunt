from tkinter import *
import mainFrame,search
def studentdata(root):
    global studataframe
    studataframe=Frame(root,width=900,height=400,bg='#1d1d1d')
    studataframe.pack(side=RIGHT, fill=Y)
    Label(studataframe, text='Search By ID', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=200, y=80)
    idquery = Entry(studataframe, font=('Helvetica', 11), textvariable=StringVar())
    idquery.place(x=350, y=80)
    idquery.insert(0,'eseee001')
    Button(studataframe, text='Search', font=('Helvetica',8), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda:searchaction1(root,idquery)).place(x=600, y=80)

    Label(studataframe, text='Search By Name', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=200, y=130)
    namequery = Entry(studataframe, font=('Helvetica', 11), textvariable=StringVar())
    namequery.place(x=350, y=130)
    Button(studataframe, text='Search', font=('Helvetica', 8), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda:searchaction2(root,namequery)).place(x=600, y=130)

    Label(studataframe, text='Search By Course', font=('Helvetica', 11), bg='#1d1d1d', fg='white').place(x=200, y=180)
    coursequery = Entry(studataframe, font=('Helvetica', 11), textvariable=StringVar())
    coursequery.place(x=350, y=180)
    Button(studataframe, text='Search', font=('Helvetica', 8), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda:searchaction3(root,coursequery)).place(x=600, y=180)

    Button(studataframe, text='Back', font=('Helvetica', 11), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda :backaction2(root)).place(x=350, y=300)
    Button(studataframe, text='Edit Data', font=('Helvetica', 11), width=11, bg='#856363', fg='#e0ebeb').place(x=600, y=300)

def studataframedest():

    studataframe.destroy()


def backaction2(root):
    studataframedest()
    mainFrame.main(root)

def searchaction1(root,idquery):
    y=idquery.get()
    studataframedest()
    x='Reg_No'
    search.searchfun(root,x,y)
def searchaction2(root,namequery):
    y=namequery.get()
    x='Student_Name'
    studataframedest()
    search.searchfun(root, x,y)
def searchaction3(root,coursequery):
    y=coursequery.get()
    x='Course'
    studataframedest()
    search.searchfun(root, x,y)

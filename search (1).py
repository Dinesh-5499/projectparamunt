from tkinter import *
from scrolling_area import *
import sqlite3
import studentData
def searchfun(root,x,y):
    global searchframe
    searchframe=Frame(root,width=900,height=400,bg='#1d1d1d')
    searchframe.pack(side=RIGHT, fill=Y)
    con=sqlite3.connect('PARAMOUNT')
    query="select * from studenttable where {}='{}'".format(x,y)
    ol=con.execute(query)
    data=[]
    for row in ol:
        column1 = []
        data.append(column1)
        for r in row:
            column1.append(r)


    scrolling_area = Scrolling_Area(searchframe, width=900, height=400)
    scrolling_area.place(x=0, y=0)
    table = Table(scrolling_area.innerframe, ['Reg. No', 'Student Name', 'Father Name', 'Hometown', 'Mobile No', 'Course','Course Fee','Fee Deposit','Remaining Fee'],
                  height=300, column_minwidths=[100, 100, 100, 100, 100, 100], stripped_rows=("#dec3c3", "#e7e3e3"),
                  header_font=('Helvetica', 8, 'bold'), cell_font=('Helvetica', 9), cell_foreground="black")
    table.pack(expand=True, fill=X)
    table.set_data(data)
    table.on_change_data(scrolling_area.update_viewport())
    Button(searchframe, text='Back', font=('Helvetica', 11), width=11, bg='#3E766D', fg='#e0ebeb',command=lambda: backaction3(root)).place(x=400, y=365)
    Button(searchframe, text='Edit Data', font=('Helvetica', 8
                                                ), width=11, bg='#856363', fg='#e0ebeb').place(x=600,y=365)


def searchframedest():

    searchframe.destroy()


def backaction3(root):
    searchframedest()
    studentData.studentdata(root)
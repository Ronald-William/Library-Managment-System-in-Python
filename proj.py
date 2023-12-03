from tkinter import *
from tkinter import messagebox
import mysql.connector as ms
import pickle
import os
mycon = ms.connect(host='localhost', user='root', passwd='qwerty')
mycursor = mycon.cursor()
mycursor.execute('use project')


def main():
    global win
    win=Tk()
    win.geometry("1000x1000")
    win.title('GUI LIBRARY')
    win.configure(bg='#0C548C')
    label = Label(win,text='SELECT USER',font=('bold',30),).pack()
    b1 = Button(win,text='ADMIN',font=('arial',20),bg='black',fg='white',command=admin)
    b1.pack(padx=50,pady=50)
    b2 = Button(win,text='CUSTOMER',font=('arial',20),bg='black',fg='white',command=customer)
    b2.pack(padx=50,pady=50)
    b3 = Button(win,text='EXIT',font=('arial',20),bg='black',fg='white',command=win.destroy)
    b3.pack(padx=50,pady=50)

def admin():
    win.destroy()
    global win2
    win2=Tk()
    win2.geometry("1000x1000")
    win2.title('GUI LIBRARY')
    win2.configure(bg='#0C548C')
    un=Label(win2,text="Enter Admin Name",font=('ariel',15),bg='white',fg='black')
    un.place(x=250,y=50)
    global un_ent
    un_ent = Entry(win2,width=35)
    un_ent.place(x=550,y=60)
    pswd = Label(win2,text="Enter Password",font=('ariel',15),bg='white',fg='black')
    pswd.place(x=250,y=100)
    global pswd_ent
    pswd_ent = Entry(win2,width = 35)
    pswd_ent.place(x=550,y=110)
    b3=Button(win2,text="Enter",width=30,height=2,command=check)
    b3.place(x=400,y=170)

def check():
    nm=un_ent.get()
    ps=pswd_ent.get()
    if nm.lower() == "r" and ps == 'q':
        win2.destroy()
        global win3
        win3=Tk()
        win3.geometry("1000x1000")
        win3.title('GUI LIBRARY')
        win3.configure(bg='#0C548C')
        label = Label(win3,text='Welcome Admin',font=('bold',30)).pack()
        b4=Button(win3,text="Book Stock",width=30,height=2,font=('ariel',13),bg='white',fg='black',command=bookstock)
        b4.place(x=360,y=100)
        b5=Button(win3,text="Record Managment",width=30,height=2,font=('ariel',13),bg='white',fg='black',command=rmanage)
        b5.place(x=360,y=250)
    else:
        messagebox.showerror(title="Error", message="Incorrect Username or Password")

def bookstock():
    win3.destroy()
    global win4
    win4=Tk()
    win4.geometry("1000x1000")
    win4.title("GUI LIBRARY")
    win4.configure(bg='#0C548C')
    label = Label(win4,text = 'Select Function',font=('ariel',25)).pack()
    b5=Button(win4,text='Add Book to Stock',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=createstock)
    b5.place(x=360,y=100)
    b7=Button(win4,text='Delete Book',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=delbook)
    b7.place(x=360,y=200)
    b8=Button(win4,text='Display Stock',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=stockview)
    b8.place(x=360,y=300)

def rmanage():
    win3.destroy()
    global win7
    win7=Tk()
    win7.geometry("1000x1000")
    win7.title("GUI LIBRARY")
    win7.configure(bg='#0C548C')
    label = Label(win7,text = 'Select Function',font=('ariel',25)).pack()
    b9=Button(win7,text='Add Record',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=createrec)
    b9.place(x=360,y=50)
    b10=Button(win7,text='Display Records',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=displayrec)
    b10.place(x=360,y=100)
    b11=Button(win7,text='Search',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=searchrec)
    b11.place(x=360,y=150)
    b13=Button(win7,text='Delete Record',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=delrec)
    b13.place(x=360,y=200)
    b14=Button(win7,text='Update Phone Number',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=updateph)
    b14.place(x=360,y=250)
    b15=Button(win7,text='Update Book Rented',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=updatebr)
    b15.place(x=360,y=300)

   

def createstock():
    global win5
    win5=Tk()
    win5.geometry("1000x1000")
    win5.title("GUI LIBRARY")
    win5.configure(bg='#0C548C')
    label=Label(win5,text="Enter Details",font=('ariel',25)).pack()
    name=Label(win5,text="Enter Name Of The Book",font=('ariel',15),bg='white',fg='black')
    name.place(x=250,y=150)
    global name_ent
    name_ent = Entry(win5,width=35)
    name_ent.place(x=550,y=160)
    author=Label(win5,text='Enter Author',font=('ariel',15),bg='white',fg='black')
    author.place(x=250,y=200)
    global author_ent
    author_ent = Entry(win5,width=35)
    author_ent.place(x=550,y=210)
    status=Label(win5,text='Available/On Rent',font=('ariel',15),bg='white',fg='black')
    status.place(x=250,y=250)
    global status_ent
    status_ent = Entry(win5,width=35)
    status_ent.place(x=550,y=260)
    b16=Button(win5,text="Enter",width=25,height=1,font=('ariel',15),bg='white',fg='black',command=stock)
    b16.place(x=400,y=300)



def delbook():
    global win9
    win9=Tk()
    win9.geometry("1000x1000")
    win9.title("GUI LIBRARY")
    win9.configure(bg='#0C548C')
    label=Label(win9,text="Enter Details",font=('ariel',25)).pack()
    name2=Label(win9,text="Enter Name Of The Book For Deletion",font=('ariel',15),bg='white',fg='black')
    name2.place(x=140,y=150)
    global name2_ent
    name2_ent = Entry(win9,width=35)
    name2_ent.place(x=550,y=160)
    b18=Button(win9,text="Enter",width=25,height=1,font=('ariel',15),bg='white',fg='black',command=del2)
    b18.place(x=400,y=300)


def stockview():
    mycursor.execute("select * from projectstock")
    mydata = mycursor.fetchall()
    if mydata == []:
        messagebox.showinfo(title="Error", message="Stock Is Empty")
    else:
        global win10
        win10=Tk()
        win10.geometry("1000x1000")
        win10.title("GUI LIBRARY")
        win10.configure(bg='#0C548C')
        label = Label(win10, text="BOOK STOCK", font=('ariel bold',25), fg='black').pack()
       
        grid = Frame(win10)
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)
        grid.columnconfigure(2, weight=1)
        x=1
        n=Label(grid,text='NAME',font=('ariel',17),bg='white',fg='black')
        n.grid(row=x,column=0,sticky=W+E)
        a=Label(grid,text='AUTHOR',font=('ariel',17),bg='white',fg='black')
        a.grid(row=x,column=1,sticky=W+E)
        s=Label(grid,text='STATUS',font=('ariel',17),bg='white',fg='black')
        s.grid(row=x,column=2,sticky=W+E)

        r=3
        for a,b,c in mydata:
            n=Label(grid,text=a,font=('ariel',15),bg='white',fg='grey')
            n.grid(row=r,column=0,sticky=W+E)
            a=Label(grid,text=b,font=('ariel',15),bg='white',fg='grey')
            a.grid(row=r,column=1,sticky=W+E)
            s=Label(grid,text=c,font=('ariel',15),bg='white',fg='grey')
            s.grid(row=r,column=2,sticky=W+E)
            r+=1
        grid.pack(fill='x')

           
def createrec():
    global win11
    win11=Tk()
    win11.geometry("1000x1000")
    win11.title("GUI LIBRARY")
    win11.configure(bg='#0C548C')
    label=Label(win11,text="Enter Details",font=('ariel',25)).pack()
    nrec=Label(win11,text="Enter Name Of The Customer",font=('ariel',15),bg='white',fg='black')
    nrec.place(x=250,y=150)
    global nrec_ent
    nrec_ent = Entry(win11,width=35)
    nrec_ent.place(x=550,y=160)
    idrec=Label(win11,text='Enter CustomerId',font=('ariel',15),bg='white',fg='black')
    idrec.place(x=250,y=200)
    global idrec_ent
    idrec_ent = Entry(win11,width=35)
    idrec_ent.place(x=550,y=210)
    dor=Label(win11,text='Date of Renting',font=('ariel',15),bg='white',fg='black')
    dor.place(x=250,y=250)
    global dor_ent
    dor_ent = Entry(win11,width=35)
    dor_ent.place(x=550,y=260)
    brec=Label(win11,text='Enter Book rented',font=('ariel',15),bg='white',fg='black')
    brec.place(x=250,y=300)
    global brec_ent
    brec_ent=Entry(win11,width=35)
    brec_ent.place(x=550,y=310)
    phrec=Label(win11,text='Phone Number',font=('ariel',15),bg='white',fg='black')
    phrec.place(x=250,y=350)
    global phrec_ent
    phrec_ent=Entry(win11,width=35)
    phrec_ent.place(x=550,y=360)
    b19=Button(win11,text="Enter",width=25,height=1,font=('ariel',15),bg='white',fg='black',command=create)
    b19.place(x=400,y=400)

def displayrec():
    mycursor.execute('Select * from projcustomer')
    mydata=mycursor.fetchall()
    if mydata==[]:
        messagebox.showinfo(title="Error", message="Stock Is Empty")
    else:
        global win12
        win12=Tk()
        win12.geometry("1000x1000")
        win12.title("GUI LIBRARY")
        win12.configure(bg='#0C548C')
        label = Label(win12, text="RENTING RECORDS", font=('ariel bold',25), fg='black').pack()
       
        grid1 = Frame(win12)
        grid1.columnconfigure(0, weight=1)
        grid1.columnconfigure(1, weight=1)
        grid1.columnconfigure(2, weight=1)
        grid1.columnconfigure(3, weight=1)
        grid1.columnconfigure(4, weight=1)
        x=0
        n=Label(grid1,text='NAME',font=('ariel',17),bg='white',fg='black')
        n.grid(row=x,column=0,sticky=W+E)
        a=Label(grid1,text='CustomerId',font=('ariel',17),bg='white',fg='black')
        a.grid(row=x,column=1,sticky=W+E)
        s=Label(grid1,text='Date OF Renting',font=('ariel',17),bg='white',fg='black')
        s.grid(row=x,column=2,sticky=W+E)
        s=Label(grid1,text='Book Rented',font=('ariel',17),bg='white',fg='black')
        s.grid(row=x,column=3,sticky=W+E)
        s=Label(grid1,text='Phone Number',font=('ariel',17),bg='white',fg='black')
        s.grid(row=x,column=4,sticky=W+E)

        r=1
        for a,b,c,d,e in mydata:
            n=Label(grid1,text=a,font=('ariel',15),bg='white',fg='grey')
            n.grid(row=r,column=0,sticky=W+E)
            a=Label(grid1,text=b,font=('ariel',15),bg='white',fg='grey')
            a.grid(row=r,column=1,sticky=W+E)
            s=Label(grid1,text=c,font=('ariel',15),bg='white',fg='grey')
            s.grid(row=r,column=2,sticky=W+E)
            s=Label(grid1,text=d,font=('ariel',15),bg='white',fg='grey')
            s.grid(row=r,column=3,sticky=W+E)
            s=Label(grid1,text=e,font=('ariel',15),bg='white',fg='grey')
            s.grid(row=r,column=4,sticky=W+E)
            r+=1
        grid1.pack(fill='x')


def searchrec():
    win13=Tk()
    win13.geometry("1000x1000")
    win13.title("GUI LIBRARY")
    win13.configure(bg='#0C548C')
    csrch=Label(win13,text='Enter CustomerId for searching',font=('ariel',15),bg='white',fg='black')
    csrch.place(x=250,y=250)
    global csrch_ent
    csrch_ent=Entry(win13,width=35)
    csrch_ent.place(x=550,y=260)
    b20=Button(win13,text="Enter",width=20,height=1,font=('ariel',15),bg='white',fg='black',command=q)
    b20.place(x=350,y=320)


def q():
    cust=csrch_ent.get()
    query = "Select * from projcustomer where CustomerId = {}".format(int(cust))
    mycursor.execute(query)
    mydata=mycursor.fetchall()
    if mydata==[]:
        messagebox.showinfo(title="Error", message="No Such Record")
    else:
        global win14
        win14=Tk()
        win14.geometry("1000x1000")
        win14.title("GUI LIBRARY")
        win14.configure(bg='#0C548C')
        label = Label(win14, text="RECORD FOUND", font=('ariel',25), fg='black').pack()

        grid2=Frame(win14)
        grid2.columnconfigure(0, weight=1)
        grid2.columnconfigure(1, weight=1)
        grid2.columnconfigure(2, weight=1)
        grid2.columnconfigure(3, weight=1)
        grid2.columnconfigure(4, weight=1)
        x=0
        n=Label(grid2,text='NAME',font=('ariel',20),bg='white',fg='black')
        n.grid(row=x,column=0,sticky=W+E)
        a=Label(grid2,text='CustomerId',font=('ariel',20),bg='white',fg='black')
        a.grid(row=x,column=1,sticky=W+E)
        s=Label(grid2,text='Date OF Renting',font=('ariel',20),bg='white',fg='black')
        s.grid(row=x,column=2,sticky=W+E)
        s=Label(grid2,text='Book Rented',font=('ariel',20),bg='white',fg='black')
        s.grid(row=x,column=3,sticky=W+E)
        s=Label(grid2,text='Phone Number',font=('ariel',20),bg='white',fg='black')
        s.grid(row=x,column=4,sticky=W+E)
       
        r=1
        for a,b,c,d,e in mydata:
   
            n=Label(grid2,text=a,font=('ariel',17),bg='white',fg='grey')
            n.grid(row=r,column=0,sticky=W+E)
            a=Label(grid2,text=b,font=('ariel',17),bg='white',fg='grey')
            a.grid(row=r,column=1,sticky=W+E)
            s=Label(grid2,text=c,font=('ariel',17),bg='white',fg='grey')
            s.grid(row=r,column=2,sticky=W+E)
            s=Label(grid2,text=d,font=('ariel',17),bg='white',fg='grey')
            s.grid(row=r,column=3,sticky=W+E)
            s=Label(grid2,text=e,font=('ariel',17),bg='white',fg='grey')
            s.grid(row=r,column=4,sticky=W+E)
            r+=1
        grid2.pack(fill='x')




def delrec():
    global win16
    win16=Tk()
    win16.geometry("1000x1000")
    win16.title("GUI LIBRARY")
    win16.configure(bg='#0C548C')
    cst1=Label(win16,text='Enter CustomerId for deletion:',font=('ariel',15),bg='white',fg='black')
    cst1.place(x=250,y=250)
    global cst1_ent
    cst1_ent=Entry(win16,width=35)
    cst1_ent.place(x=550,y=260)
    b22=Button(win16,text="Enter",width=20,height=1,font=('ariel',15),bg='white',fg='black',command=delete)
    b22.place(x=400,y=400)


def updateph():
    global win17
    win17=Tk()
    win17.geometry("1000x1000")
    win17.title("GUI LIBRARY")
    win17.configure(bg='#0C548C')
    cst2=Label(win17,text='Enter CustomerId for Updation:',font=('ariel',15),bg='white',fg='black')
    cst2.place(x=250,y=250)
    global cst2_ent
    cst2_ent=Entry(win17,width=35)
    cst2_ent.place(x=550,y=260)
    phn=Label(win17,text='Enter New Phone Number:',font=('ariel',15),bg='white',fg='black')
    phn.place(x=250,y=300)
    global phn_ent
    phn_ent=Entry(win17,width=35)
    phn_ent.place(x=550,y=310)
    b23=Button(win17,text="Enter",width=20,height=1,font=('ariel',15),bg='white',fg='black',command=upd)
    b23.place(x=400,y=400)
   

def updatebr():
    global win18
    win18=Tk()
    win18.geometry("1000x1000")
    win18.title("GUI LIBRARY")
    win18.configure(bg='#0C548C')
    br=Label(win18,text='Enter Currently Rented Book:',font=('ariel',15),bg='white',fg='black')
    br.place(x=250,y=250)
    global br_ent
    br_ent=Entry(win18,width=35)
    br_ent.place(x=550,y=260)
    br2=Label(win18,text='Enter Newly Rented Book:',font=('ariel',15),bg='white',fg='black')
    br2.place(x=250,y=300)
    global br2_ent
    br2_ent=Entry(win18,width=35)
    br2_ent.place(x=550,y=310)
    b24=Button(win18,text="Enter",width=20,height=1,font=('ariel',15),bg='white',fg='black',command=upd2)
    b24.place(x=400,y=400)

def customer():
    win.destroy()
    global win19
    win19=Tk()
    win19.geometry("1000x1000")
    win19.title("GUI LIBRARY")
    win19.configure(bg='#0C548C')
    label = Label(win19,text = 'Select Function',font=('ariel',25)).pack()
    b25=Button(win19,text='View Books',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=viewstock)
    b25.place(x=360,y=100)
    b26=Button(win19,text='Search For A Book',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=searchstock)
    b26.place(x=360,y=200)
    b27=Button(win19,text='Rent A Book',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=rentbook)
    b27.place(x=360,y=300)
    b28=Button(win19,text='Exit',width=30,height=2,font=('ariel',13),bg='white',fg='black',command=destroy)
    b28.place(x=360,y=400)

def destroy():
    win19.destroy()
   
def viewstock():
    mycursor.execute("select * from projectstock")
    mydata = mycursor.fetchall()
    if mydata == []:
        messagebox.showinfo(title="Error", message="Stock Is Empty")
    else:
        global win20
        win20=Tk()
        win20.geometry("1000x1000")
        win20.title("GUI LIBRARY")
        win20.configure(bg='#0C548C')
        label = Label(win20,text="BOOK STOCK",font=("ariel",25)).pack()
       
        grid2 = Frame(win20)
        grid2.columnconfigure(0, weight=1)
        grid2.columnconfigure(1, weight=1)
        grid2.columnconfigure(2, weight=1)
        x=1
        n=Label(grid2,text='NAME',font=('ariel',17),bg='white',fg='black')
        n.grid(row=x,column=0,sticky=W+E)
        a=Label(grid2,text='AUTHOR',font=('ariel',17),bg='white',fg='black')
        a.grid(row=x,column=1,sticky=W+E)
        s=Label(grid2,text='STATUS',font=('ariel',17),bg='white',fg='black')
        s.grid(row=x,column=2,sticky=W+E)

        r=3
        for a,b,c in mydata:
            n=Label(grid2,text=a,font=('ariel',15),bg='white',fg='grey')
            n.grid(row=r,column=0,sticky=W+E)
            a=Label(grid2,text=b,font=('ariel',15),bg='white',fg='grey')
            a.grid(row=r,column=1,sticky=W+E)
            s=Label(grid2,text=c,font=('ariel',15),bg='white',fg='grey')
            s.grid(row=r,column=2,sticky=W+E)
            r+=1
        grid2.pack(fill='x')

def searchstock():
    win21=Tk()
    win21.geometry("1000x1000")
    win21.title("GUI LIBRARY")
    win21.configure(bg='#0C548C')
    bk2=Label(win21,text='Enter Name Of The Book',font=('ariel',15),bg='white',fg='black')
    bk2.place(x=250,y=250)
    global bk2_ent
    bk2_ent=Entry(win21,width=35)
    bk2_ent.place(x=550,y=260)
    b29=Button(win21,text="Enter",width=20,height=1,font=('ariel',15),bg='white',fg='black',command=s)
    b29.place(x=350,y=320)

def s():
    bname=bk2_ent.get()
    query = "Select * from projectstock where BookName = '{}'".format(bname)
    mycursor.execute(query)
    mydata=mycursor.fetchall()
    if mydata==[]:
        messagebox.showinfo(title="Error", message="No Such Record")
    else:
        global win12
        win22=Tk()
        win22.geometry("1000x1000")
        win22.title("GUI LIBRARY")
        win22.configure(bg='#0C548C')
        label = Label(win22, text="RECORD FOUND", font=('ariel',25), fg='black').pack()

        grid2=Frame(win22)
        grid2.columnconfigure(0, weight=1)
        grid2.columnconfigure(1, weight=1)
        grid2.columnconfigure(2, weight=1)
     
        x=0
        n=Label(grid2,text='BOOK NAME',font=('ariel',20),bg='white',fg='black')
        n.grid(row=x,column=0,sticky=W+E)
        a=Label(grid2,text='AUTHOR',font=('ariel',20),bg='white',fg='black')
        a.grid(row=x,column=1,sticky=W+E)
        s=Label(grid2,text='STATUS',font=('ariel',20),bg='white',fg='black')
        s.grid(row=x,column=2,sticky=W+E)
   
        r=1
        for a,b,c in mydata:
   
            n=Label(grid2,text=a,font=('ariel',17),bg='white',fg='grey')
            n.grid(row=r,column=0,sticky=W+E)
            a=Label(grid2,text=b,font=('ariel',17),bg='white',fg='grey')
            a.grid(row=r,column=1,sticky=W+E)
            s=Label(grid2,text=c,font=('ariel',17),bg='white',fg='grey')
            s.grid(row=r,column=2,sticky=W+E)
            r+=1
        grid2.pack(fill='x')

def rentbook():
    global win23
    win23=Tk()
    win23.geometry("1000x1000")
    win23.title("GUI LIBRARY")
    win23.configure(bg='#0C548C')
    bkn=Label(win23,text='Enter Name Of The Book',font=('ariel',15),bg='white',fg='black')
    bkn.place(x=250,y=250)
    global bkn_ent
    bkn_ent=Entry(win23,width=35)
    bkn_ent.place(x=550,y=260)
    at=Label(win23,text='Enter Name Of The Author',font=('ariel',15),bg='white',fg='black')
    at.place(x=250,y=300)
    global at_ent
    at_ent=Entry(win23,width=35)
    at_ent.place(x=550,y=310)
    b30=Button(win23,text="Enter",width=20,height=1,font=('ariel',15),bg='white',fg='black',command=rent)
    b30.place(x=350,y=360)


def rent():
    chng='on rent'
    bk=bkn_ent.get()
    at=at_ent.get()
    s = open('stk.dat', 'rb+')
    flag = False
    d = {}
    l = []
    try:
        while True:
            rec = pickle.load(s)
            if rec['book'] == bk.title() and rec['author'] == at.title():
                flag = True
                pass
            else:
                l.append(rec)
    except EOFError:
        s.close()
        if flag == False:
            messagebox.showinfo(title="Error", message="Sorry we don't have that right now")
        elif rec['status']=='on rent':
            messagebox.showinfo(title="Error", message="Sorry we the book is not available right now")
        elif flag == True:
            f = open('stk.dat', 'wb')
            for x in l:
                f = open('stk.dat', 'wb')
                for x in l:
                    pickle.dump(x, f)
                d['book'] = bk.title()
                d['author'] = at.title()
                d['status'] = 'on rent'
                pickle.dump(d, f)
                f.close()                                
                query = "update projectstock set status = '{}' where BookName = '{}'".format(chng,bk)
                mycursor.execute(query)
                mycon.commit()
            messagebox.showinfo(title="Info", message="Rented succesfully")



def delete():
    f = open('lib.dat', 'rb')
    n = open('abc.dat', 'wb')
    flag = False
    d = {}
    cst=int(cst1_ent.get())
    try:
        while True:
            st = pickle.load(f)
            if st['customer id'] == cst:
                flag = True
                pass
            else:
                d = st
                pickle.dump(d, n)
    except EOFError:
        f.close()
        n.close()
        os.remove('lib.dat')
        os.rename('abc.dat', 'lib.dat')
        if flag == False:
            messagebox.showerror(title="Error", message="Invalid Customer Id")
           
        else:
            query = "delete from projcustomer where CustomerId = {}".format(cst)
            mycursor.execute(query)
            mycon.commit()
            messagebox.showinfo(title="Info", message="RECORD DELETED")

def upd():
    f = open('lib.dat', 'rb+')
    cst = int(cst2_ent.get())
    ph2 = phn_ent.get()
    flag = False
    try:
        while True:
            pos = f.tell()
            st = pickle.load(f)
            if st['customer id'] == cst:
                st['phone number'] = ph2
                f.seek(pos)
                pickle.dump(st, f)
                flag = True
    except EOFError:
        f.close()
        if flag == False:
            messagebox.showerror(title="Error", message="Invalid Customer Id")
           
        else:
            print('UPDATION COMPLETE')
            query = "update projcustomer set PHNo = {} where CustomerID = {}".format(ph2, cst)
            mycursor.execute(query)
            mycon.commit()
            messagebox.showinfo(title="Info", message="PHONE NUMBER UPDATED")

def upd2():
    f = open('lib.dat', 'rb+')
    b1 = br_ent.get()
    b2 = br2_ent.get()
    flag = False
    try:
        while True:
            pos = f.tell()
            st = pickle.load(f)
            if st['book rented'] == b1:
                st['book rented'] = b2
                f.seek(pos)
                pickle.dump(st, f)
                flag = True
    except EOFError:
        f.close()
    if flag == False:
        messagebox.showerror(title="Error", message="NO SUCH BOOK AVAILABLE")
       
    else:
        print('UPDATION COMPLETE')
        query = "update projcustomer set BOOK = '{}' where BOOK = '{}'".format(b2,b1)
        mycursor.execute(query)
        mycon.commit()
        messagebox.showinfo(title="Info", message="RENTED BOOK UPDATED")


def create():
    f = open('lib.dat', 'ab+')
    st = {}
    name = nrec_ent.get()
    custid = int(idrec_ent.get())
    date = dor_ent.get()
    bn = brec_ent.get()
    ph = phrec_ent.get()
    st['name'] = name
    st['customer id'] = custid
    st['Date of renting'] = date
    st['book rented'] = bn
    st['phone number'] = ph
    pickle.dump(st, f)
    f.close()
    try:
        mycursor.execute('create table projcustomer(Name varchar(30),customerid integer NOT NULL PRIMARY KEY,DOR date NOT NULL,Book varchar(50),PHno integer NOT NULL)')
    except:
       pass
    query = "insert into projcustomer values('{}',{},'{}','{}',{})".format(name, custid, date, bn, ph)
    mycursor.execute(query)
    mycon.commit()

    messagebox.showinfo(title="Info", message="RECORD INSERTED")
    nrec_ent.delete(0, 'end')
    idrec_ent.delete(0, 'end')
    dor_ent.delete(0, 'end')
    brec_ent.delete(0, 'end')
    phrec_ent.delete(0, 'end')
    n = open('lib.dat','rb')
    try:
        while True:
            s=pickle.load(n)
            print(s)
    except EOFError:
        n.close()
    


def stock():
    stock = open('stk.dat', 'ab')
    d = {}
    bk = name_ent.get()
    at = author_ent.get()
    st = status_ent.get()
    d['book'] = bk.title()
    d['author'] = at.title()
    d['status'] = st.title()
    pickle.dump(d, stock)
    stock.close()
    try:
        mycursor.execute('create table Projectstock(BookName varchar(30), Author varchar(30), status varchar(20))')
    except:
        pass
    query = "insert into projectstock values('{}','{}','{}')".format(bk, at, st)
    mycursor.execute(query)
    mycon.commit()
    messagebox.showinfo(title="Info", message="RECORD INSERTED")
    name_ent.delete(0,'end')
    author_ent.delete(0,'end')
    status_ent.delete(0,'end')

   

def del2():
    stock = open('stk.dat', 'rb')
    random = open('xyz.dat', 'wb')
    flag = False
    d = {}
    bk=name2_ent.get()
    try:
        while True:
            st = pickle.load(stock)
            if st['book'] == bk.title():
                flag = True
                pass
            else:
                d = st
                pickle.dump(d, random)
    except EOFError:
        if flag == False:
            print('NO SUCH ENTRY')
        else:
            stock.close()
            random.close()
            os.remove('stk.dat')
            os.rename('xyz.dat', 'stk.dat')
            query = "delete from projectstock where BookName = '{}'".format(bk)
            mycursor.execute(query)
            mycon.commit()
            messagebox.showinfo(title="Info", message="RECORD DELETED")
            win9.destroy()
           
 

   

main()

    

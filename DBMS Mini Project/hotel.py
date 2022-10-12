import mysql.connector
import tkinter
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user=YOUR_USERNAME_HERE,
  password=YOUR_PASSWORD_HERE
)

mycursor = mydb.cursor()
mycursor.execute("USE trial")

def reg():
  nm=e1.get()
  ag=e2.get()
  addr=e3.get()
  cin=e4.get()
  cout=e5.get()

  sql=("INSERT INTO hotel (name,age,address,ckin,ckout) VALUES (%s,%s,%s,%s,%s)")
  val=(nm,ag,addr,cin,cout)
  try:
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Success', 'Registered Successfully')
  except:
      mydb.rollback()
      messagebox.showerror('Error','Please Insert Correct Data')
  res()

def res():
  e1.delete(0, END)
  e2.delete(0, END)
  e3.delete(0, END)
  e4.delete(0, END)
  e5.delete(0, END)

def calc():
  nam=e1.get()

  sql=("SELECT ckin FROM hotel WHERE name=%s")
  mycursor.execute(sql,(nam,))
  result=mycursor.fetchall()
  date1=[x[0] for x in result]
  d1=date1[0]

  sql=("SELECT ckout FROM hotel WHERE name=%s")
  mycursor.execute(sql,(nam,))
  result=mycursor.fetchall()
  date2=[x[0] for x in result]
  d2=date2[0]

  diff=(d2-d1).days

  base=diff*1500                   #Rs 1500 per day
  gst=(18*base)/100
  total=base+gst

  sql = ("UPDATE hotel SET bill=%s WHERE name=%s")
  val = (total, nam)
  try:
      mycursor.execute(sql,val)
      mydb.commit()
      messagebox.showinfo('TOTAL BILL ',total)
  except:
      mydb.rollback()
      messagebox.showerror('Error','Please Insert Correct Data')
  res1()

def res1():
  e1.delete(0, END)


while(True):
    print("1. Hotel Booking")
    print("2. Hotel Bill Calculator")
    print("3. Exit")
    a=int(input("Please Enter Your Choice: "))
    if(a==1):
        win = tkinter.Tk()
        win.geometry("800x700")
        win.title("Paradise Hotel")
        win.configure(background="#000000")

        lbl = Label(
            win,
            text=("Registration"),
            font=("Verdana", 16),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl.pack(pady=50)

        lbl2 = Label(
            win,
            text=('Name'),
            font=("Comic sans ms", 14),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl2.pack()

        e1 = Entry(
            win,
            font=("Verdana")
        )
        e1.pack(pady=7, ipadx=5, ipady=5)

        lbl3 = Label(
            win,
            text=('Age (In Years)'),
            font=("Comic sans ms", 14),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl3.pack()

        e2 = Entry(
            win,
            font=("Verdana")
        )
        e2.pack(pady=7, ipadx=5, ipady=5)

        lbl4 = Label(
            win,
            text=('Address'),
            font=("Comic sans ms", 14),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl4.pack()

        e3 = Entry(
            win,
            font=("Verdana")
        )
        e3.pack(pady=7, ipadx=5, ipady=5)

        lbl5 = Label(
            win,
            text=('Check-In Date (YYYY-MM-DD)'),
            font=("Comic sans ms", 14),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl5.pack()

        e4 = Entry(
            win,
            font=("Verdana")
        )
        e4.pack(pady=7, ipadx=5, ipady=5)

        lbl6 = Label(
            win,
            text=('Check-Out Date (YYYY-MM-DD)'),
            font=("Comic sans ms", 14),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl6.pack()

        e5 = Entry(
            win,
            font=("Verdana")
        )
        e5.pack(pady=7, ipadx=5, ipady=5)

        b1 = Button(
            win,
            text=("Register"),
            font=("Caomic sans ms", 12),
            width=14,
            bg=("#4C4B4B"),
            fg=("#6ab04c"),
            relief="raised",
            command=reg
        )
        b1.pack(pady=15)

        win.mainloop()
    elif(a==2):
        win = tkinter.Tk()
        win.geometry("600x500")
        win.title("Paradise Hotel")
        win.configure(background="#000000")

        lbl = Label(
            win,
            text=("Bill Calculator"),
            font=("Verdana", 16),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl.pack(pady=50)

        lbl2 = Label(
            win,
            text=('Please Enter Your Name'),
            font=("Comic sans ms", 14),
            bg=("#000000"),
            fg=("#ffffff")
        )
        lbl2.pack()

        e1 = Entry(
            win,
            font=("Verdana")
        )
        e1.pack(pady=7, ipadx=5, ipady=5)

        b1 = Button(
            win,
            text=("Calculate"),
            font=("Caomic sans ms", 12),
            width=14,
            bg=("#4C4B4B"),
            fg=("#6ab04c"),
            relief="raised",
            command=calc
        )
        b1.pack(pady=15)

        win.mainloop()
    elif(a==3):
        print("Thank You!!")
        break
    else:
        print("Invalid Input")

from tkinter import *
import datetime

root = Tk()
root.title('Age Calculator')
root.geometry('400x300')

frame = Frame(master=root, height=200, width=360, bg='#FFC300')

lbl1 = Label(frame, text="Year", bg="#CD5C5C", fg='white', width=10)
lbl2 = Label(frame, text="Month", bg="#CD5C5C", fg='white', width=10)
lbl3 = Label(frame, text="Date", bg="#CD5C5C", fg='white', width=10)

year_entry = Entry(frame)
month_entry = Entry(frame)
date_entry = Entry(frame)


def calculate():
    year = int(year_entry.get())
    today = datetime.date.today()
    age = today.year - year  
    message = ("Your age is", age)
    textbox.insert(END, message)
    
textbox = Text(root, bg="#BEBEBE", fg="black")
btn = Button(root, text="Calculate", command=calculate, bg="blue")

frame.place(x=20, y=20)


lbl1.place(x=25, y=20)
year_entry.place(x=150, y=20)
lbl2.place(x=25, y=50)
month_entry.place(x=150, y=50)
lbl3.place(x=25, y=80)
date_entry.place(x=150, y=80)
btn.place(x=140, y=140)
textbox.place(y=250)

root.mainloop()
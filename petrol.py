from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
root = tk.Tk()
root.title("Charge explorer")
root.geometry("950x500+200+100")
root.resizable(False,False)
root.configure(background="slate gray")

p1 = PhotoImage(file = 'p1.jpg')
root.iconphoto(False, p1)


#main window
photo = tk.PhotoImage(file =r"C:\Users\Riddhi\Pictures\p1.jpg")

photo1 = tk.PhotoImage(file =r"C:\Users\Riddhi\Pictures\p2.jpg")

l1 = Label(root,text="Charge Explorer",font=("arial",16,'bold'),bg="black",fg="white",width=15,cursor="dot",relief=SUNKEN,borderwidth=6)
l2 = Label(root,text="Petrol",font=("arial",16,'bold'),fg="seashell4",bg="black",cursor="dot",width=10,relief=SUNKEN,borderwidth=6)
l3 = Label(root,text="Electricity",font=("arial",16,'bold'),fg="seashell4",bg="black",cursor="dot",width=10,relief=SUNKEN,borderwidth=6)
b1 = Button(root, text="",image=photo,width=180,compound=BOTTOM,relief=RAISED,borderwidth=6,\
cursor="hand2")
b2 = Button(root, text="",image=photo1,width=180,compound=BOTTOM,relief=RAISED,borderwidth=6,\
cursor="hand2")


l1.grid(row=1,column=3,padx=5,pady=25)
l2.grid(row=2,column=2,padx=5,pady=5)
l3.grid(row=2,column=4,padx=5,pady=5)

b1.grid(row=4,column=2,padx=90,pady=0)
b2.grid(row=4,column=4,padx=90,pady=0)



root.mainloop()
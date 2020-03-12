from tkinter import *
import time
import tkinter.font


global second 
master=Tk()

master.configure(background='black')
my3=font.Font(family='Helvetic',size=15,weight=font.BOLD)

def Time():
    second=1200
    for i in range(second):
            num=str(second-i)
            l1.config(text=num+" second",fg="RED",font=my3)           
            time.sleep(1)
            master.update()
            
def o():
   b.pack_forget()
#   b1=Button(master,height=1,width=10,text="Restart",activebackground="LIGHT GREEN")
#   b1.pack()
   Time()

Label(master,text="Blink Your Eye in: ",bg='BLACK',fg='WHITE',font=my3).pack()
l1=Label(master,height=4,width=20,bg="BLACK")
l1.pack() 

b=Button(master,height=1,width=10,text="Click to start",command=o,activebackground="LIGHT GREEN")
b.pack(side=LEFT)

Button(master,text="Cancel",command=master.destroy,height=1,width=10,activebackground="RED").pack(side=RIGHT)

master.mainloop()

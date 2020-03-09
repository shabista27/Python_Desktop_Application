from tkinter import *
import random
import tkinter.font


root=Tk()
root.geometry("5000x4100")

my = font.Font(family='Courier', size=95, weight=font.BOLD,underline=1)
my2 =font.Font(family='Courier', size=15, weight=font.BOLD)
my3=font.Font(family='Helvetic',size=30,weight=font.BOLD)
   
count=0

def next():

    top=Toplevel()
    top.geometry("700x500")
   
    r = 0
    c = 0
    n = 1
    global r1;
    r1=[]
   
    list=[]
   
    top.title("Page 1")
    root.title("Random_Number")
   
    my = font.Font(family='Courier', size=95, weight=font.BOLD,underline=1)
    my2 =font.Font(family='Courier', size=15, weight=font.BOLD)
    my3=font.Font(family='Helvetic',size=20,weight=font.BOLD)
   
    b=Label(top,text='The number is : ',font=my3)
    b.grid()
       
   
    global number;
   
    for i in range(1,460):
              r=random.randint(1,90)
              if r not in list:
                  list.append(r)
   
    for n in range(1,91):
            b=Button(top,text=(str(n)),width=10,font=my2)
            b.grid(row=r,column=c)
            r1.append(b)
            n += 1
            c += 1
            if c>7:
                c=0
                r+=1  
     
   
       
       
    def d():
        global number;
        number.destroy()
        global count
        i=0
        #print("n",num)
        #print("c",count)
        if count < 100:
               
                num=list.pop(i)
                number=Button(top,text=num,fg="red",command=d,font=my)
                number.grid(row=0,column=1,sticky='E')
                count+=1  
                r1[num-1].config(bg='sky blue')
                i+=1
   
   
       
    num=list.pop()
    count=0
    number=Button(top,text=num,fg="red",command=d,font=my)
    number.grid(row=0,column=1,sticky='E')  
    r1[num-1].config(bg='sky blue')
   
   
   
    button = Button(top, text='Stop',bg='light yellow',width=5,command=root.destroy)
    button.grid(row=0,column=70)





c=Label(root,text='TAMBOLA....',font=my3)
c.grid(row=30, column=50)

e=Label(root,text='\n\n\n\nPress start button to start the game....',font=my3)
e.grid(row=100, column=50)
start = Button(root, text='Start',bg='light green',width=50,height=2,command=next)
start.grid(row=210,column=70)
stop = Button(root, text='Exit',bg='light yellow',width=50,height=2,command=root.destroy)
stop.grid(row=250,column=70)

root.mainloop()


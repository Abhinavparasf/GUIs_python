from tkinter import *
import math
root = Tk()
root.geometry("600x700")
#root.maxsize(600, 600)
root.title("Area calculator")
root.wm_iconbitmap("2.ico")
root.configure()
l1 = Label(root,text="Welcome to Area Calculator",font=("Cooper Black",25,"bold"),borderwidth=8,relief=GROOVE)
l1.pack(padx=15,fill="x",pady=15)
l2 = Label(root,text="Choose figure",font=("Elephant",20,"bold"),borderwidth=6,relief=RIDGE)
l2.pack(anchor="w",pady=20,padx=15)
var = IntVar()
r1 = Radiobutton(root,text="Rectangle",variable=var,value=1,font=("Constantia",13))
r1.pack(anchor="w",padx=15)

r2 = Radiobutton(root,text="Square",variable=var,value=2,font=("Constantia",13))
r2.pack(anchor="w",padx=15)

r3 = Radiobutton(root,text="Triangle",variable=var,value=3,font=("Constantia",13))
r3.pack(anchor="w",padx=15)

r4 = Radiobutton(root,text="Circle",variable=var,value=4,font=("Constantia",13))
r4.pack(anchor="w",padx=15)

r5 = Radiobutton(root,text="Regular hexagon",variable=var,value=5,font=("Constantia",13))
r5.pack(anchor="w",padx=15)

def display():
    global f
    if var.get() == 1:
        f = Frame(root)
        l1 = Label(f,text="Enter length  :  ",font=("Constantia",13))
        l1.grid(row=0)
        l2 = Label(f,text="Enter width   :  ",font=("Constantia",13))
        l2.grid(row=1)
        ar = Label(f,text="Area          :  ",font=("Constantia",13))
        ar.grid(row=2)
        length = DoubleVar()
        width = DoubleVar()
        area = StringVar()
        l = Entry(f,textvariable=length)
        l.grid(row=0,column=1)
        w = Entry(f,textvariable=width)
        w.grid(row=1,column=1)
        a = Entry(f,textvariable=area)
        a.grid(row=2,column=1)

        def calculate():
            area1 = length.get() * width.get()
            area.set(str(area1))

        def clear():
            length.set(0.0)
            width.set(0.0)
            area.set("")
        cal = Button(f,text="Calculate",font=("Constantia",13),relief=RAISED,borderwidth=2,command=calculate)
        cal.grid(row=3)
        clr = Button(f,text="Clear",font=("Constantia",13),relief=RAISED,borderwidth=2,command=clear,width=8)
        clr.grid(row=3,column=1)
        f.pack(anchor="w",pady=15,padx=15)

    if var.get() == 2:
        f = Frame(root)
        s = Label(f, text="Enter side  :  ",font=("Constantia",13))
        s.grid(row=0)
        ar = Label(f, text="Area         :  ",font=("Constantia",13))
        ar.grid(row=1)
        side = DoubleVar()
        area = StringVar()
        l = Entry(f, textvariable=side)
        l.grid(row=0, column=1)
        a = Entry(f, textvariable=area)
        a.grid(row=1, column=1)

        def calculate():
            area1 = side.get() * side.get()
            area.set(str(area1))

        def clear():
            side.set(0.0)
            area.set("")
        cal = Button(f,text="Calculate",font=("Constantia",13),relief=RAISED,borderwidth=2,command=calculate)
        cal.grid(row=2)
        clr = Button(f, text="Clear", font=("Constantia", 13), relief=RAISED, borderwidth=2, command=clear,width=8)
        clr.grid(row=2, column=1)
        f.pack(anchor="w",pady=15,padx=15)

    if var.get() == 3:
        f = Frame(root)
        l1 = Label(f, text="Enter 1st side  :  ", font=("Constantia",13))
        l1.grid(row=0)
        l2 = Label(f, text="Enter 2nd side  :  ", font=("Constantia", 13))
        l2.grid(row=1)
        l3 = Label(f, text="Enter 3rd side  :  ", font=("Constantia", 13))
        l3.grid(row=2)
        a = Label(f, text="Area            :  ", font=("Constantia",13))
        a.grid(row=3)
        side1 = DoubleVar()
        side2 = DoubleVar()
        side3 = DoubleVar()
        area = StringVar()
        s1 = Entry(f, textvariable=side1, font=("Constantia", 13))
        s1.grid(row=0, column=1)
        s2 = Entry(f, textvariable=side2, font=("Constantia", 13))
        s2.grid(row=1, column=1)
        s3 = Entry(f, textvariable=side3, font=("Constantia", 13))
        s3.grid(row=2, column=1)
        a = Entry(f, textvariable=area, font=("Constantia", 13))
        a.grid(row=3, column=1)

        def calculate():
            s = (side1.get()+side2.get()+side3.get())/2
            area1 = math.sqrt(s*(s-side1.get())*(s-side2.get())*(s-side3.get()))
            area.set(str(area1))

        def clear():
            side1.set(0.0)
            side2.set(0.0)
            side3.set(0.0)
            area.set("")
        cal = Button(f, text="Calculate", font=("Constantia", 13), relief=RAISED, borderwidth=2, command=calculate)
        cal.grid(row=4)
        clr = Button(f, text="Clear", font=("Constantia", 13), relief=RAISED, borderwidth=2, command=clear,  width=8)
        clr.grid(row=4, column=1)
        f.pack(anchor="w", pady=15, padx=15)
    if var.get()==4:
        f = Frame(root)
        r = Label(f, text="Enter radius  :  ", font=("Constantia", 13))
        r.grid(row=0)
        ar = Label(f, text="Area         :  ", font=("Constantia", 13))
        ar.grid(row=1)
        radius = DoubleVar()
        area = StringVar()
        r1 = Entry(f, textvariable=radius)
        r1.grid(row=0, column=1)
        a = Entry(f, textvariable=area)
        a.grid(row=1, column=1)

        def calculate():
            area1 = math.pi * radius.get() * radius.get()
            area.set(str(area1))

        def clear():
            radius.set(0.0)
            area.set("")
        cal = Button(f, text="Calculate", font=("Constantia", 13), relief=RAISED, borderwidth=2, command=calculate)
        cal.grid(row=2)
        clr = Button(f, text="Clear", font=("Constantia", 13), relief=RAISED, borderwidth=2, command=clear,width=8)
        clr.grid(row=2, column=1)
        f.pack(anchor="w", pady=15, padx=15)

    if var.get() == 5:
        f = Frame(root)
        h = Label(f, text="Enter side  :  ", font=("Constantia", 13))
        h.grid(row=0)
        ar = Label(f, text="Area         :  ", font=("Constantia", 13))
        ar.grid(row=1)
        height = DoubleVar()
        area = StringVar()
        h1 = Entry(f, textvariable=height)
        h1.grid(row=0, column=1)
        a = Entry(f, textvariable=area)
        a.grid(row=1, column=1)

        def calculate():
            area1 = (math.sqrt(3) * height.get() * height.get())/4
            area.set(str(area1))

        def clear():
            height.set(0.0)
            area.set("")
        cal = Button(f, text="Calculate", font=("Constantia", 13), relief=RAISED, borderwidth=2, command=calculate)
        cal.grid(row=2)
        clr = Button(f, text="Clear", font=("Constantia", 13), relief=RAISED, borderwidth=2, command=clear,width=8)
        clr.grid(row=2, column=1)
        f.pack(anchor="w",pady=15, padx=15)


def cancel():
    f.destroy()


b1 = Button(root,text="OK",font=("Constantia",13),width=14,relief=RAISED,borderwidth=2,command=display)
b1.pack(anchor="w",padx=15,pady=10)
b2 = Button(root,text="Cancel",font=("Constantia",13),width=14,relief=RAISED,borderwidth=2,command=cancel)
b2.pack(anchor="w",pady=3,padx=15)
lbl = Label(root,text="NOTE : kindly click on cancel button before going to another figure.Thank you!",font=("Comic sans ms",10))
lbl.pack(anchor="w",padx=15,pady=3)
root.mainloop()

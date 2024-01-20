from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
# root.maxsize(1000, 700)
root.minsize(800, 700)
root.title("To do list")
root.wm_iconbitmap("to_do_icon.ico")
root.config(bg="#730e44")

l1 = Label(text="TO DO LIST", fg="#61320c", bg="#209eba", borderwidth=3, relief=RAISED, font="Cambria 20 bold")
l1.pack(pady=20, ipady=5, ipadx=70)

f = Frame(root)
f.pack(pady=15)

box = Listbox(f, height=10, width=30, font=("Comic Sans MS", 16), bg="#1c3b31", fg="#adf0e1", activestyle="none")
box.pack(side="left", fill=BOTH)
sb = Scrollbar(f)
sb.pack(side=RIGHT, fill=BOTH)
box.config(yscrollcommand=sb.set)
sb.config(command=box.yview)

l2 = Label(root, text="type work here", bg="#8feb98", fg="#8f3013", borderwidth=3, relief=RIDGE,
           font="Cambria 16 bold")
l2.pack(pady=5, anchor="center", ipadx=53)

entry = Entry(root, font=("Comic Sans MS", 16), width=30)
entry.pack(pady=5, anchor="center")

f1 = Frame(root)
f1.pack(pady=7)

work = []
for j in work:
    box.insert(END, j)


def add_item():
    tsk = entry.get()
    if tsk != "":
        box.insert(END, tsk)
        entry.delete(0, END)
    else:
        messagebox.showwarning("warning", "Please enter work")


def delete_item():
    box.delete(ANCHOR)


add_btn = Button(f1, text="Add work", width=15, height=2, font=("HP Simplified", 14), command=add_item,
                 relief=GROOVE, bg="#d49ee8", fg="#3d0f06")
add_btn.pack(side="left", fill="both")
delete_btn = Button(f1, text="Delete work", width=15, height=2, font=("HP Simplified", 14), command=delete_item,
                    relief=GROOVE, bg="#767fdb", fg="#451f08")
delete_btn.pack(side="left", fill="both")
root.mainloop()

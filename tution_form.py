from tkinter import *
root = Tk()
root.geometry("800x800")
root.title("Admission form")
n = Label(text="F     I     I     T     J     E     E", bg="yellow", fg="red", borderwidth=8, font="Castellar 30 bold", padx=5, pady=5)
n.grid(row=0, column=1)
l1 = Label(text="Welcome to FIITJEE. Premier institute for IIT JEE ", fg="red", font="arial 20 bold")
l1.grid(row=2, column=1)
l2 = Label(text="For admission, Please fill this form.", fg="red", font="Corbel 20 bold")
l2.grid(row=3, column=1)
name = Label(root, text="Name", borderwidth=5, relief=SUNKEN, padx=27)
name.grid(row=5, column=1)
std = Label(root, text="Standard", borderwidth=5, relief=SUNKEN, padx=19)
std.grid(row=6, column=1)
mn = Label(root, text="Mobile Number", borderwidth=5, relief=SUNKEN)
mn.grid(row=7, column=1)
city = Label(root, text="City", borderwidth=5, relief=SUNKEN, padx=32)
city.grid(row=8, column=1)
mail = Label(root, text="Mail ID", borderwidth=5, relief=SUNKEN, padx=24)
mail.grid(row=9, column=1)
name_val = StringVar()
std_val = StringVar()
mn_val = StringVar()
city_val = StringVar()
mail_val = StringVar()
name_ent = Entry(root, textvariable=name_val)
std_ent = Entry(root, textvariable=std_val)
mn_ent = Entry(root, textvariable=mn_val)
city_ent = Entry(root, textvariable=city_val)
mail_ent = Entry(root, textvariable=mail_val)
name_ent.grid(row=5, column=2)
std_ent.grid(row=6, column=2)
mn_ent.grid(row=7, column=2)
city_ent.grid(row=8, column=2)
mail_ent.grid(row=9, column=2)


def sub():
    print("Congratulations,Successfully submitted!!")


b1 = Button(root, text="Submit", command=sub)
b1.grid(row=10, column=2)


def save_info():
    f = open("form_1.txt", "a")
    str1 = "\n"+"Name : "+str(name_val.get())+"\n"+"Standard : "+str(std_val.get())+"\n"+"Mobile No. : "+str(mn_val.get())+"\n"
    str2 = "City : "+str(city_val.get())+"\n"+"Mail : "+str(mail_val.get())+"\n"
    str3 = str1+str2
    f.write(str3)
    f.close()


b2 = Button(root, text="Save", command=save_info, padx=8)
b2.grid(row=11, column=2)
root.mainloop()

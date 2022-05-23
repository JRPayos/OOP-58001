from tkinter import *
window = Tk()
window.title("Smallest Number Finder")
window.geometry("400x200+550+300")

def LNfinder():
    L = []
    L.append(eval(num1.get()))
    L.append(eval(num2.get()))
    L.append(eval(num3.get()))
    LeastNumber.set(min(L))

lbl1 = Label(window, text="This Program finds the least number among three numbers", fg="white", bg="blue", font=("Verdana", 10))
lbl1.grid(row=0, column=0, columnspan=2)

#First number
lbl2 = Label(window, text="Enter the first number:")
lbl2.grid(row=1, column=0, sticky=W)
num1 = StringVar()
ent2 = Entry(window, bd=3, textvariable=num1)
ent2.grid(row=1, column=1)

#Second number
lbl3 = Label(window, text="Enter the second number:")
lbl3.grid(row=2, column=0, sticky=W)
num2=StringVar()
ent3 = Entry(window, bd=3, textvariable=num2)
ent3.grid(row=2, column=1)

#Third number
lbl4 = Label(window, text="Enter the third number:")
lbl4.grid(row=3, column =0, sticky=W)
num3 = StringVar()
ent4 = Entry(window, bd=3, textvariable=num3)
ent4.grid(row=3, column=1)

#Smallest number
btn1 = Button(window, text="Find the smallest #", command=LNfinder)
btn1.grid(row=4, column=1)
lbl5 = Label(window, text="The smallest number:")
lbl5.grid(row=5, column=0, sticky=W)
LeastNumber = StringVar()
ent5 = Entry(window, bd=3, state="readonly", textvariable=LeastNumber)
ent5.grid(row=5, column=1)

mainloop()
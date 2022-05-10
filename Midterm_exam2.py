from tkinter import*

window = Tk()

window.geometry("500x300")
window.title("Midterm OOP")

def name_text():
    textfield2.insert(END, textfield1.get())

#label
label = Label(window, text="Enter your fullname:", fg="red")
label.place(x=50, y=50)

#textfield1
name1 = StringVar()
textfield1 = Entry(window, bd=5, textvariable=name1)
textfield1.place(x=250, y=50)

#button
button = Button(window, text="Click to display your Fullname", fg="red", command=name_text)
button.place(x=50, y=100)

#textfield2
name2 = StringVar()
textfield2 = Entry(window, bd=5, textvariable=name2)
textfield2.place(x=250, y=100)


window.mainloop()
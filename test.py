from tkinter import *
parent = Tk()
parent.geometry('500x500')
button1 = Button(parent, text = 'click me!', fg='red', highlightbackground='yellow' )
button1.pack()
print(button1["highlightbackground"])
parent.mainloop()
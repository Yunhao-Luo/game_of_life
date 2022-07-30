import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
parent = tk.Frame(root)

buttonNames = ['numberOne','numberTwo','happyButton']
buttonDic = {}
buttonColors = {}

def change_color(name):
    buttonColors[name].set("red")
    buttonDic[name].config(background=buttonColors[name].get())

for name in buttonNames:
    buttonColors[name] = tk.StringVar()
    buttonColors[name].set("blue")
    buttonDic[name] = ttk.Button(
            parent,
            text = name,
            width = 20,
            background = buttonColors[name].get(),
            command= lambda passName=name: change_color(passName)
            )

parent.grid(row=0,column=0)
for i,name in enumerate(buttonNames):
    buttonDic[name].grid(row=i,column=0)

time.sleep(1)
change_color('numberOne')

root.mainloop()
from tkinter import *

cb_strings = ['item 1', 'item 2', 'item 3', 'item 4']

opt = ''


def sel():
    opt = str(var.get())


root = Tk()
var = StringVar()
var.set(cb_strings[0])

monitor = Label(root, text=opt)
monitor.pack()

for item in cb_strings:
    button = Radiobutton(root, text=item, variable=var,
                         value=item, command=sel)
    button.pack(anchor=W)


root.mainloop()

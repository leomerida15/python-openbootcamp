from tkinter import Entry, Tk, W, E, Button

from inserts import Insert


root = Tk()

root.title = 'calculator'

display = Entry(root)

insert = Insert(display)

display.grid(row=1, columnspan=6, sticky=W+E)

# Number Buttons

# row 2
Button(root, text='1', command=lambda: insert.addItem('1')).grid(row=2, column=0)
Button(root, text='2', command=lambda: insert.addItem('2')).grid(row=2, column=1)
Button(root, text='3', command=lambda: insert.addItem('3')).grid(row=2, column=2)

# row 3
Button(root, text='4', command=lambda: insert.addItem('4')).grid(row=3, column=0)
Button(root, text='5', command=lambda: insert.addItem('5')).grid(row=3, column=1)
Button(root, text='6', command=lambda: insert.addItem('6')).grid(row=3, column=2)

# row 4
Button(root, text='7', command=lambda: insert.addItem('7')).grid(row=4, column=0)
Button(root, text='8', command=lambda: insert.addItem('8')).grid(row=4, column=1)
Button(root, text='9', command=lambda: insert.addItem('9')).grid(row=4, column=2)

Button(root, text='0', command=lambda: insert.addItem(
    '0')).grid(row=5, column=0, sticky=W+E)
# row 5


# Bottom Buttons
Button(root, text="AC", command=lambda: insert.clear()).grid(row=5, column=0)
Button(root, text="0", command=lambda: insert.addItem(
    '0')).grid(row=5, column=1)
# Button(root, text="%", command=lambda: get_operation("%")).grid(row=5, column=2)

# Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
# Button(root, text="-", command=lambda: get_operation("-")
#        ).grid(row=3, column=3, sticky=W+E)
# Button(root, text="*", command=lambda: get_operation("*")
#        ).grid(row=4, column=3, sticky=W+E)
# Button(root, text="/", command=lambda: get_operation("/")
#        ).grid(row=5, column=3, sticky=W+E)

# # More Math Operators
# Button(root, text="⟵", command=lambda: undo()).grid(
#     row=2, column=4, sticky=W+E, columnspan=2)
# Button(root, text="exp", command=lambda: get_operation(
#     "**")).grid(row=3, column=4)
# Button(root, text="^2", command=lambda: get_operation(
#     "**2")).grid(row=3, column=5)
# Button(root, text="(", command=lambda: get_operation(
#     "(")).grid(row=4, column=4, sticky=W+E)
# Button(root, text=")", command=lambda: get_operation(
#     ")")).grid(row=4, column=5, sticky=W+E)
# Button(root, text="=", command=lambda: calculate()).grid(
#     row=5, column=4, sticky=W+E, columnspan=2)


root.mainloop()

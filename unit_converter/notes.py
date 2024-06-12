"""
Working with Tkinter GUI
"""
# Pull all tkinter and no longer needs module.property syntax
from tkinter import *

window = Tk()
window.title("My first GUI program!")
window.minsize(width=900, height=700)

# Label - first create and then specify the layout on screen
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

# pack will automatically center
# my_label.pack()

# Change text property with keyword or config
my_label["text"] ="New Text"
my_label.config(text="New Text")

# Entry
input_box = Entry(width=20)
input_box.focus()
# input_box.pack()

# Multi-line textbox
text = Text(height=5, width= 30)
text.insert(END, "Enter more text here")
# get current value of line 1, char 1 - starting point, ending point
print(text.get("1.0", END))
# text.pack()

# Button
def button_click():
    print("I got clicked")
    # Returns input as a string
    input_text = input_box.get()
    my_label.config(text=input_text)



# Grid - uses column and row to place items, this relative to the widget
test_label = Label(text="Hey there!")
test_label.grid(column=0, row=0)
test_label.config(padx=10, pady=10)

button = Button(text="Click", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="Click", command=button_click)
new_button.grid(column=2, row=0)

# pack(),place(),grid() layout managers
new_text = Entry(width= 20)
# Use place to give x,y - place is very specific
# new_text.place(x=0,y=0)
new_text.grid(column=3, row=3)

# Add padding to the window
window.config(padx=300, pady=300)

# mainloop keeps window on screen - always at end of program
window.mainloop()

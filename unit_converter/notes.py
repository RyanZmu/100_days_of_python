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
my_label.pack()

# Change text property with keyword or config
my_label["text"] ="New Text"
my_label.config(text="New Text")

# Button
button = Button(text="Click")
button.pack()



# mainloop keeps window on screen - alwasy at end of program
window.mainloop()

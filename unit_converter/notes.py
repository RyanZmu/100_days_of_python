"""
Working with Tkinter GUI
"""
import tkinter

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=900, height=700)


# Label - first create and then specify the layout on screen
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

# pack will automatically center
my_label.pack()


"""
Default and keywords
**kw and **args lets you have default arguments for functions that dont need specifying every function call

When you see a argument that looks like this: arg=... it means there is a default value for that argument
Can set what arguments are required and what ones are optional and are defaulted

This will allow you to set default arguments and require arguments with each function
"""
# *args

# Create a function that takes unlimited arguments - use *args and loop the arguments, now any amount of arguments can be used
def add(*args):
    for n in args:
        print(n)

add(1,10,2)
# mainloop keeps window on screen - alwasy at end of program
window.mainloop()

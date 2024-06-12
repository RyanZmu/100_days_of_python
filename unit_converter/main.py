"""
Miles to Kilometer unti converter
Stretch: Add more units to convert (in to cm)

Make a GUI for a user to enter in Miles and have it converted to Kilometer
"""

from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=100, height=200)
window.config(padx=60, pady=60)


# Define functions
result = 0
def convert_units():
    number = int(unit_field.get())
    result = number * 1.6093445
    print(result)
    results_label.config(text=f"is equal to {result}")
    return result


# Define UI components
unit_field = Entry(width=20)
unit_field.focus()
calculate_button = Button(text="Calculate", command=convert_units)
miles_label = Label(text= "Miles")
km_label = Label(text="Kilometers")
results_label = Label()

# Place UI components
unit_field.grid(column=0, row=0)
miles_label.grid(column=1, row=0)
km_label.grid(column=1, row=1)
results_label.grid(column=0, row=1)
calculate_button.grid(column=0, row=2)


window.mainloop()
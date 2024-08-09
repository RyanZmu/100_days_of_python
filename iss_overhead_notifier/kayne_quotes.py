# Create a simple UI for Kanye quotes
# Use Kanya API
# Raise an exception if we get unsuccessful return code
# Parse JSON for quote text
# Display with the canvas quote_text widget
from tkinter import *
import requests

# =========== Functions ===============
def get_quote():
    global quote
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()

    quote = data["quote"]

    canvas.itemconfig(text_box, text=quote)


# =========== UI Setup ===============
window = Tk()
window.title("Kanye Says..")
window.config(height=900, width=600, pady=50)

canvas = Canvas(height=570, width=600)
quote_box = PhotoImage(file="./iss_overhead_notifier/images/background.png")
kanye = PhotoImage(file="./iss_overhead_notifier/images/kanye.png")
canvas.create_image(310, 350, image=quote_box)
text_box = canvas.create_text(310,350, text="Click on Kayne!", font=("Arial",24,"bold"),fill="white", width=250)

kayne_button = Button(image=kanye, command=get_quote)

canvas.grid(column=1, row=1)
kayne_button.grid(column=1, row=2)

# get_quote()

window.mainloop()
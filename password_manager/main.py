from tkinter import *
from tkinter.messagebox import *
from random import shuffle, choice, randint
import pyperclip
import json

#--------------Password Generator------------#
def generate_password():
    global password_field_text

    NUM_LIST: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LETTER_LIST: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                        'U', 'V', 'W', 'X', 'Y', 'Z']
    SYMBOLS_LIST: list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    # Create a list of possible chars to be used in final password
    char_pool: list = []

    # Number ranges for characters
    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    # Find x amount of random numbers - range = number of times to repeat
    password_letters = [choice(LETTER_LIST) for _ in range(nr_letters)]
    password_numbers = [choice(NUM_LIST) for _ in range(nr_numbers)]
    password_symbols = [choice(SYMBOLS_LIST) for _ in range(nr_symbols)]

    # Reorder the char_pool to make a random password
    char_pool = password_letters + password_numbers+ password_symbols
    shuffle(char_pool)
    final_password = "".join(char_pool)

    password_field_text.insert(0, final_password)

    # Copy password to clipboard
    pyperclip.copy(final_password)

#--------------Save Password-----------#
# Take inputs and save them to a file after add is pressed
# username | email | password data.txt
def update_pass_file():
    global website_text, email_and_username_text, password_field_text

    # Get values from fields
    website = website_text.get()
    email_and_username_value = email_and_username_text.get()
    password_value = password_field_text.get()

    # Gather form data for json
    new_data = {
        website: {
                "email": email_and_username_value,
                "password": password_value,
        }
    }

    # Check if fields are blank
    if len(website) == 0 or len(email_and_username_value) == 0 or len(password_value) == 0:
        showwarning(
            title="Invalid Entries",
            message="You have left one or more fields blank")
    else:
        # # Confirm user wants to save
        save_message = askokcancel(
            title="Confirm Save",
            message=f"Are you sure you want to save this?\n Website: {website}\n Email/Username: {email_and_username_value}\n Password:{password_value}")

        if save_message:
            # Write to file
            try:
                with open("./password_manager/data.json", "r") as password_file:
                    # Reading current data
                    data = json.load(password_file)
            except FileNotFoundError:
                with open("./password_manager/data.json", "w") as password_file:
                    # Adds data to new file
                    json.dump(new_data, password_file, indent=4)
            else:
                with open("./password_manager/data.json", "w") as password_file:
                    # Check if data exists, ask for overwrite if needed - checks for key in dict
                    if website in data:
                        overwrite_message = askokcancel(
                            title="Confirm Overwrite",
                            message=f"Save data exists for {website}.\n Overwrite this data?")
                        if overwrite_message:
                            # Updating old data with new data
                            data.update(new_data)
                            # Saving updated data if overwrite accepted
                            json.dump(data, password_file, indent=4)
                        else:
                            # Dump current data back in with no changes (Erases file data if this is excluded)
                            json.dump(data, password_file, indent=4)
                    else:
                        # Saving updated data and add to password file
                        data.update(new_data)
                        json.dump(data, password_file, indent=4)
            finally:
                # Remove text in fields
                website_text.delete(0, END)
                password_field_text.delete(0, END)
        else:
            pass


def search_password():
    global website_text

    website = website_text.get()

    try:
        with open("./password_manager/data.json", "r") as password_file:
            data = json.load(password_file)
            requested_website = data[website]
    except KeyError:
        showwarning(
            title="Password Not Found",
            message=f"There is no password associated with the website {website}!")
    except FileNotFoundError:
        showwarning(
            title="No Password Data",
            message="Failed to find password data; You must save a password first!")
    else:
        showinfo(
            title=f"{website}",
            message=f"Email: {requested_website["email"]}\n Password: {requested_website["password"]}"
        )

#--------------UI Setup-----------#
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = Canvas(height=200, width=200)
lock_image = PhotoImage(file="password_manager/images/lock_logo.png")
logo.create_image(100, 100, image=lock_image)

# Fields
website = Label(text="Website")
website_text = Entry(width=35)
website_text.focus()

email_and_username = Label(text="Email/Username")
email_and_username_text = Entry(width=35)
email_and_username_text.insert(0, "ryanzmudka@gmail.com")

password_field = Label(text="Password")
password_field_text = Entry(width=35)

# Buttons
password_gen_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add",width=36, command=update_pass_file)
search_button = Button(text="Search", command=search_password)

# Layout
logo.grid(column=1, row=0)
website.grid(column=0,row=1)
website_text.grid(column=1, row=1, columnspan=2)
search_button.grid(column=3,row=1)
email_and_username.grid(column=0, row=2)
email_and_username_text.grid(column=1, row=2, columnspan=2)
password_field.grid(column=0,row=3)
password_field_text.grid(column=1, row=3, columnspan=2)
password_gen_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
from tkinter import *
from random import choice
import pandas

# ========== Read Data ==========
# Use original translation data file if no saved file found
# If the words_to_learn file is empty because all have been completed - then use original file to restart the cards
try:
    translation_data = pandas.read_csv(filepath_or_buffer="./flashcards_german/data/words_to_learn.csv")
    print("Using saved data")
except FileNotFoundError and pandas.errors.EmptyDataError:
    translation_data = pandas.read_csv(filepath_or_buffer="./flashcards_german/data/German_To_English_Words.csv")
    print("Using original translation data")
    to_learn = translation_data.to_dict(orient="records")
else:
    to_learn = translation_data.to_dict(orient="records")

current_card = {}

# ========== Functions ==========
def get_next_card():
    global current_card, flip_timer, to_learn
    # Cancel the timer on click
    window.after_cancel(flip_timer)
    try:
        current_card = choice(to_learn)
    except IndexError:
        print("out of words")
        # Reset card data to original file
        translation_data = pandas.read_csv(filepath_or_buffer="./flashcards_german/data/German_To_English_Words.csv")
        to_learn = translation_data.to_dict(orient="records")

    # Update card text
    card.itemconfig(card_image, image=flash_card_front_image)
    card.itemconfig(language_text, text="German")
    card.itemconfig(current_word, text=f"{current_card["German"]}")

    # Flip after 3 seconds if no button is clicked
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    card.itemconfig(language_text, text="English", fill="white")
    card.itemconfig(current_word, text=f"{current_card["English"]}", fill="white")
    card.itemconfig(card_image, image=flash_card_back_image)

def on_check():
    global current_card
    # On check, word is removed from the possible words to display
    to_learn.remove(current_card)
    print(to_learn)

    get_next_card()

def on_cross():
    global translation_data, to_learn
    # Create csv of the remaining words to learn
    new_data = pandas.DataFrame(data=to_learn)
    new_data.to_csv(path_or_buf="./flashcards_german/data/words_to_learn.csv", index=False)
    get_next_card()



# ========== UI Setup ==========
window = Tk()
BACKGROUND_COLOR = "#B1DDC6"
window.title("German to English Flashcards")
window.config(padx=100, pady=75, bg=BACKGROUND_COLOR)

# Flip card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Get images
flash_card_front_image = PhotoImage(file="./flashcards_german/images/card_front.png")
flash_card_back_image = PhotoImage(file="./flashcards_german/images/card_back.png")
check_mark_image = PhotoImage(file="./flashcards_german/images/right.png")
cross_image = PhotoImage(file="./flashcards_german/images/wrong.png")

# Flash Card
card = Canvas(height=700, width=900, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(500,350, image=flash_card_front_image)
language_text = card.create_text(500, 300, text="German", font=("Arial", 18, "italic"))
current_word = card.create_text(500, 400, text=current_card, font=("Arial", 24, "bold"))

# Buttons
check_button = Button(image=check_mark_image, command=on_check)
cross_button = Button(image=cross_image, command=on_cross)


card.grid(column=0,row=0, columnspan=2)
check_button.grid(column=1, row=1)
cross_button.grid(column=0, row=1)

# Start first flash card
get_next_card()

window.mainloop()
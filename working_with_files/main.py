"""
Birthday invite challenge
- Create invites for each name in the invited_names file
- Move the completed invites to ReadyToSend
"""

# Create a variable of invited guests - readline to make into a list of names
with open(file="./working_with_files/birthday_card/Input/Names/invited_names.txt") as invited_file:
    invited_guests = invited_file.readlines()


# Format the list to remove \n and any white spaces left over
formatted_list = []
for guest in invited_guests:
    formatted_guest = guest.replace("\n", "").strip()
    formatted_list.append(formatted_guest)


# Write names to the file and move to ReadyToSend
for guest in formatted_list:
    # Open and read the content of starting letter, save to var
    with open(file="./working_with_files/birthday_card/Input/Letters/starting_letter.txt", mode="r") as letter:
        line_to_replace = letter.read()

    # Open and replace name in var with guest name, save as a new text file
    with open(file=f"./working_with_files/birthday_card/Output/ReadyToSend/invite_{guest}.txt", mode="w") as invite:
        invite.write(line_to_replace.replace("[name]", guest))

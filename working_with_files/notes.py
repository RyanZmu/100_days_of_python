# Reading a file - using open directly means you have to close it as well, see below for alternative
# file = open(file="working_with_files/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Opening a file with the with method instead to avoid needing file.close()
with open(file="working_with_files/my_file.txt") as new_file:
    new_contents = new_file.read()
    print(new_contents)


# Writing to a file - use mode, a = append
with open(file="working_with_files/my_file.txt", mode="a") as file:
    file.write("\n New Text")


# If opening a file in write mode when it does not exist, will create the file
with open(file="working_with_files/new_file.txt", mode="w") as file:
    file.write("New File!")

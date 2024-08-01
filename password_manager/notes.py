# Exception Notes
# FileNotFound example
# bare except clause on its own ignores ALL errors - not ideal
# try:
#     file = open("a.txt")
#     a_dict = {"key": "value"}
#     # a_dict["ada"]
# except FileNotFoundError:
#     # Create the file if it doesn't exist
#     file = open("a.txt", "w")
#     file.write("Something something something")
# except KeyError as error_message:
#     # Bring in error_message to use in output
#     print(f"The key {error_message} does not exist")
# else:
#     # Read file if found
#     content = file.read()
#     print(content)
# finally:
#     # Close the file always
#     file.close()
#     print("<File was closed>")
#     # Create an exception
#     raise KeyError("Made up error")

# height = float((input("Height: ")))
# weight = int((input("Weight: ")))

# # Try to filter out unrealistic height (>3meters)
# if height > 3:
#     raise ValueError("Human heights should not be over 3 meters")

# bmi = weight / height ** 2
# print(bmi)

# Challenge - Stop the below code from failing.
# If user chooses a bad index just say Fruit"pie"
# fruits = ["Apple", "Pear", "Cherry"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as error_message:
#         print("Fruit Pie!")
#         print("Error! You entered an invalid fruit!")
#     else:
#         print(fruit + " Pie!")

# # make_pie(1)
# make_pie(1)

# Challenge - Fix the below function to handle a KeyError
facebook_posts = [{"Likes": 21, "Comments": 2}, {"Likes": 31, "Comments": 12, "Shares": 31}, {"Likes": 1, "Comments": 1}, {"Comments": 2, "Shares":2}, {"Comments": 5, "Shares": 5}]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        # If post has no likes, keep total_likes as 0
        pass

print(f"Total Likes: {total_likes}")

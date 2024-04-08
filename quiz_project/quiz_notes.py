# Class creation
class User:
    # init called everytime new object is made from class
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1 = User(user_id="001", username= "ryan")
user_2 = User(user_id="002", username= "bill")

user_1.follow(user_2)

print(user_1.following, user_1.followers)

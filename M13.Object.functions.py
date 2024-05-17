# class Animal:
#     def __init__(self, type, voice):
#         self.type = type
#         self.voice = voice

#     def speak(self):
#         print(self.voice)
# kind = input("Enter kind of animal: ")
# sound = input("Enter sound type: ")

# aOne = Animal(kind, sound)
# print(aOne.voice)
# print(aOne.type)
# aOne.speak()

class user:
    def __init__(self, firstname, lastname, likesCount, friendsName):
        self.firstname = firstname
        self.lastname = lastname
        self.likesCount = likesCount
        self.friendsName  = friendsName

    def intro(self):
        print("Hello I Am " +  self.firstname)
       
    def fullProfile(self):
        print("Full name: " + self.firstname + " " + self.lastname)
        print("Likes: " + self.likesCount)
        print("Friends: ")
        for friends in self.friendsName:
            print(" - " + friends)

fname = input("Enter first name: ")
lname = input("Enter last name: ")
likes = input("Enter Likes: ")

userOne = user(fname, lname, likes,["Jack", "Greg", "Pab"]) 
userOne.intro()
userOne.fullProfile()


    



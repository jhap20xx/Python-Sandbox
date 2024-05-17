# age = int(input("Enter age here: "))
# height = int(input("Enter height here: "))
# gend = str(input("Enter gender here: "))

# sex = ["Male" , "Female"]

# print("Age: " + str(age))


# if age >= 18 or age >= 20 and height >= 170:
#         print(" A person that is tall and on legal age")
# elif age >= 13 and  height >= 150:
#         print("A teenager with an average height")
# elif age >= 5:
#         print("A short child")
# else:
#         print("Not on legal age")

# if gend == "Male" in sex:
#         print("The person is a Male")
# else:
#         print("The person is a Female")
# print("Thank you")

# if not age >= 18:
#     print("not on legal age")
# else:
#     print("on legal age")


eng = float(input("Enter grade in English: "))
fil = float(input("Enter grade in Filipino: "))
sci = float(input("Enter grade in Science: " ))

sum = ( eng + fil + sci ) / 3


print("Your average grade is: " + str(sum))

if sum >= 100 or sum <= 50:
    print("Invalid Grade")
elif sum >= 98:
    print("With Highest honor")
elif sum >= 95:
    print("With high honor")
elif sum >= 90:
    print("With Honors")
elif sum >= 75:
    print("Passed")
elif sum <= 74:
    print("Failed")



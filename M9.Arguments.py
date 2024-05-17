

# def names(*firstnames,lastname):
#     for name in firstnames:
#          print("Hello! " + name + " " + lastname)

# fname = input("Enter Name: ")
# lname = input("Enter Last name: ")
    

# names(fname, lastname=lname)

# def student(**info):
#     print("Hello " + info["firstname"])
#     print("Your age is  " + info["age"])

# fname = input("Enter Name: ")
# age = input("Enter Age: ")
# student(firstname=fname, age=age)


# def add(*numbers):
#     for num in numbers:
#         return num + num

# numInput = float(input("Enter number: "))

# sum = add(numInput)

# print(sum)


def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return print("The sum is " + str(sum))

numbers = []

while True:
    numInput = int(input("Enter number: "))
    numbers.append(numInput)

    response = input("Do you want to enter additional number? (yes/no): ").strip().lower()
    if response == "no":
        add(*numbers)
        break
    elif response != "yes":
        print("Invalid input")

        
        
  



        

        









    


from math import sqrt   

def sayHello(fname):
    print("Hello " + fname)

name = input("Enter name: ")

sayHello(name)

def add(num1, num2):
    return num1 + num2

sum = add(5,5)
print(sum)

def isLegal(age):
    if age >= 18:
        return print(str(age) + " is a legal age")
    else:
        return print(str(age) + " is not a legal age")
    
ageInput = int(input("Enter age: "))

isLegal(ageInput)


def square(sqr):
    sqare_root = sqrt(num)
    return print("The square root of " + str(num) + " is " + str(sqare_root))

num = int(input("Enter number for square root: "))
square(num)



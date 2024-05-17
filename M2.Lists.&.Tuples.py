print("Hello Python")
print(" ")
fruits = ["Apple", "Orange", "Banana", "Mango", "Cherry"]

print("Available fruits: " + str(fruits))
print(" ")
print("Item number 4 is: " + str(fruits[3]))
print(" ")
print("item number 1 to 3 is: " + str(fruits[:3]))
print(" ")
print("item number 2 and 3 is: " + str(fruits[1:3]) )
print(" ")
fruits[1] = "Kiwi"
print("Item number 2 changed to =  " + str(fruits[1]))
print(" ")
print("Available fruits: " + str(len(fruits)) + " " + str(fruits))
print(" ")
print("Their is only " + str(fruits.count("Apple")) + " Apple on the items")
print(" ")
fruits.append("Apple")
print("Another Apple has been added to the items")
print(" ")
print("Now there are " + str(fruits.count("Apple")) + " Apple's on the items")
print(" ")
print(fruits)
fruits.insert(1, "Orange")
print(" ")
print("One item has been inserted between the Apple and Kiwi")
print(" ")
print(fruits)
fruits.remove("Cherry")
print("Cherry was remmoved")
print(" ")
print(fruits)
print(" ")
fruits.pop(0)
print("The first Apple has been successfully popped!")
print(fruits)
print(" ")

del fruits[0]
print("Orange was deleted")
print("Fruits: " + str(fruits))
print(" ")
fruits1 = fruits.copy()
print("fruits copied from lists")
print("Fruits 1: " + str(fruits1))

fruits2 = ["Grapes", "Dew"]
print("Fruits 2: " + str(fruits2))
print(" ")

Cart = fruits1 + fruits2
print("The two list fruits have been combined into Cart")
print("Cart: " + str(Cart))
print(" ")

drinks = ["Water" , "Soda"]

Cart.extend(drinks)
print("Lists of drinks have been added to cart")
print(Cart)
print(" ")
Cart.reverse()
print("The lists of drinks have been made first from the Cart")
print(Cart)
print(" ")

number  = [1, 2, 5, 4, 3]

number.sort()

print(number)

number.sort(reverse=True)

print(number)
print(" ")

Cart.append(drinks)

print(Cart)

print(str(Cart[2]) + " and " + str(Cart[8][1]))

letter = ("A", "B", "C")

print(letter[0])
print(" ")
print(number)
print(letter)
print(" ")
number = tuple(number)
letter = list(letter)
print(number)
print(letter)
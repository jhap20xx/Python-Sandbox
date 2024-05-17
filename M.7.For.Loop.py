# num = [1,2,3,4,5,6,7,8,9,0]

# for i in num:
#     if i % 2 == 0:
#         print("Even number " + str(i))
#     else:
#         print("Odd number " + str(i))

letter = ["A", "B", "C"]
number = ["1", "2", "3"]

letInput = input("Enter Letter: ")
numInput = input("Enter Number: ")

for x in range(len(letter)):
    if letInput == letter[x] and numInput == number[x]:
        print("First index match!")
        break
else:
    print("Index do not match")
    

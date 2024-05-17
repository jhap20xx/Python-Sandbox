# num = [1 , 2, 3, 4, 5]

# i = 0

# while i < len(num):
#     if num[i] % 2 == 0:
#         print("Even Nnumber " + str(num[i]))
#     else:
#         print("Odd Number " + str(num[i]) )
#     i = i + 1

tries = 2

print("You have 3 attempts to answer a math question")
print(" ")
while tries >= 0:

        print("What is the sum of 1 + 1?")
        sum = int(input("Enter answer:"))

        if sum == 2:
            print("Correct!")
            break
        else:
        
            print("not the right answer")
            print("You have " + str(tries) + " tries left")
            
        tries = tries - 1 

  
      

       
        
  






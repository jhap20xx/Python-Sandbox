print(" ")
print("Calculator")
print(" ")

class calculator:
    def __init__(self,firstNum,op,secondNum):
        self.firstNum = firstNum
        self.op = op
        self.secondNum = secondNum

    def add(self):
        sum = self.firstNum + self.secondNum
        print(f"The sum of {self.firstNum} + {self.secondNum} is {sum}")
    
    def diff(self):
        diff = firstNum - secondNum
        print(f"The difference of {self.firstNum} - {self.secondNum} is {diff}")
    
    def mul(self):
       mul = firstNum * secondNum
       print(f"{self.firstNum} multiplied by {self.secondNum} is {mul}")

    def div(self):
        if self.secondNum != 0:
            div = firstNum / secondNum
            print(f"{self.firstNum} divided by {self.secondNum} is {div}")
        else:
            print("Division by zero is not allowed.")
    

while True:  
    print(" ")
    print("Enter 000 to exit")
    firstNum = input("Enter firstnumber: ")
    if firstNum == 000:
         break
    try:
        firstNum = int(firstNum) 
    except ValueError:
        print("Invalid Input, numbers only!")
        break

    op = input("Enter operand: ")
    secondNum = input("Enter second number ")
    
    try:
        secondNum = int(secondNum)
    except ValueError:
         print("Invalid Input, numbers only!")
         break

    total = calculator(firstNum,op,secondNum)
    if op == "+":
        total.add()
    elif op == "-":
        
        total.diff()
    elif op == "*":
       
        total.mul()
    elif op == "/":
        total.div()
    else:
        print("Invalid operand")
    
   




    
    
     






        
        
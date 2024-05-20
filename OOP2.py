# class Person:
#     def __init__(self,fname):
#         self.fname = fname
      
#     def intro(self):
#         print("I am " + self.fname)
    
# listUser = []

# for i in range(3):
#     fname = input("Enter Name: ")
#     p = Person(fname)
#     listUser.append(p)

# for person in listUser:
#     person.intro()


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def con(self):
        print(self.fname + " " + self.lname + " has been added to records.")

studentRecords = []

class Students(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
    def con(self):
        super().con()  # No need to return here

while True:
    
    fname = input("Enter First Name (or type 'exit' to quit): ")
    if fname.lower() == "exit":
        break
    lname = input("Enter Last Name: ")
    print("Type 'exit' to exit")
    pup = Students(fname, lname)
    studentRecords.append(pup)

    for stud in studentRecords:
        stud.con()

print("\nStudent Records:")
for x in studentRecords:
    print(f"{x.fname} {x.lname}")



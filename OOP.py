class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def intro(self):
        print(("Hi I am " + self.fname + " " + self.lname))


class student(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname, lname)
        self.id = id

    def intro(self):
        super().intro()
        print("ID number : " + str(self.id))

        # print(("Hi I am " + self.fname + " " + self.lname + " ID number: " + str(self.id)))


stud = student("Jack", "Son", 123)
stud.intro()

class employee(student):
    def __init__(self, fname, lname, id):
       super().__init__(fname, lname, id)

    def intro(self):
        return super().intro()
    
emp = employee("Pab","Lo", 456)
emp.intro()



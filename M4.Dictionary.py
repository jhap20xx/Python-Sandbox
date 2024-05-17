score = {
    "python": 80,
    "java" : 85
}

studOne = {
    "name"   : "Greg",
    "course" : "BSIT",
    "age"    : 20,
    "grade" : score
}

studTwo = {
    "name"   : "Pab",
    "course" : "BSCS",
    "age"    : 21
}

print(studOne)
print(studTwo)

print(studOne["name"])
print(studTwo.get("name"))

studOne["age"] = 23

print(studOne)

print(len(studTwo))

studOne["gender"] = "Male"

print(studOne)

studOne.pop("gender")

print(studOne)

print(studTwo.keys())

students = [studOne, studTwo]

print(students)

print(students[1].get("name"))

print(studOne)

print(studOne.get("grade").get("java"))



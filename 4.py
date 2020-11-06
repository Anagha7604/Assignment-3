 #7

def displayStudent(name, age):
    print(name, age)
displayStudent("Eddygrant", 25)
showStudent = displayStudent
showStudent("Eddygrant" ,25)

#9

def string_test(s):
    count = {"UPPER_CASE": 0, "LOWER_CASE" :0}
    for case in s:
        if case.isupper():
            count["UPPER_CASE"] +=1
        elif case.islower():
            count["LOWER_CASE"] +=1
        else:
            pass
    print("original string :", s)
    print("No. of Uppercase Characters :", count["UPPER_CASE"])
    print("No. of Lowercase Characters :", count["LOWER_CASE"])
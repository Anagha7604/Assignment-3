#1
SkillSanta_Dict = {
    "name" : "Sachin",
    "age" : 22,
    "salary" : 60000,
    "city" : "New Delhi"
      
}
SkillSanta_Dict["Location"] = SkillSanta_Dict.pop("city")
print(SkillSanta_Dict)

#2
list = [11, 45, 8, 11, 23, 45, 89]
print(list)
count = dict()
for i in list:
    if(i in count):
        count[i] += 1
    else:
        count[i] = 1
print("Printing count of each item", count)

#3
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
print(sampleList)
sampleList = set(sampleList)
print("unique items ", sampleList)
tuple = tuple(sampleList)
print("tuple", tuple)
print("max : ", max(tuple))
print("min : ", min(tuple))

#4

def showEmployee(name, salary = 50000):
    print("Employee", name, "salary is:", salary)
showEmployee("Eddy",50000)
showEmployee("Eddy")

#5

def outerfunction(a,b):
    square = a**2
    def innerfunction(a,b):
        return a+b
    add = innerfunction(a,b)
    return add+5
sum = outerfunction(10,10)
print(sum)

#6

def fib(n):
    if n<= 1:
        return n
    return fib(n-1)+fib(n-2)
n = int(input("Enter number of terms :"))
print("Fibonacci Sequence :")
for i in range(n):
    print(fib(i))

#7

def displayStudent(name, age):
    print(name, age)
displayStudent("Eddygrant", 25)
showStudent = displayStudent
showStudent("Eddygrant" ,25)

#9

def string(s):
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



# Practical no 2
import math
num = int(input("Enter the Number :"))
print("The Square of the Number is : ",math.pow(num,2))
print("The Cube of the Number is : ",math.pow(num,2))

str = "Hello my name is Shreyash   "

print(str.strip())
print(str.capitalize())
print(str.casefold())
print(str.find("Shreyash"))
print(str.upper())


# List

list = [1,31,24,23,63,"shreyash",15.532,True]

for a in range(len(list)):
    print(list[a])

print(list[2:5])
list.append(23)
list.insert(6,"ingle")
print(list)


# Tuple

tuple = (1,31,24,23,63,"shreyash",15.532,True)
for a in range(len(tuple)):
    print(tuple[a])

print(tuple[2:5])


#Dictionary

dict = {"Fname":"Shreyash","MiddleName":"Rajesh","Lname":"Ingle"}
print(dict["MiddleName"])
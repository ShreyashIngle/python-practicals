# Practical No 9

list = [12,41,54.22,"shreyash",'S',False]
print(list)

# adding element...
list.append("Added element")
print(list)

# adding element in a specific position..
list.insert(4,"Rajesh Ingle")
print(list)

# deleting a element...
list.remove(41)
print(list)

# sorting the list...
a = [25,54,14,42,335,145,12]
a.sort()
print("Sorted List: ",a)

# reversing the list
reverse = list[::-1]
print("Reversed list: ",reverse)

# counting elements in list
ele = len(list)
print("The number of elements in the list is: ",ele)
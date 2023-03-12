# Practical No 12
arr = {}

num = int(input("How many elements you want to insert: "))

for a in range(0,num):
    key = str(input("Enter the Key: "))
    value = str(input("Enter the Value: "))
    arr[key] = value

print(arr)

rem = str(input("Enter the key you want to delete from the dictionary: "))

arr.pop(rem)
print("After removing the Key from the Dictionary: ")
print(arr)
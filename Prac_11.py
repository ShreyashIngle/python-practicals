# Practical No 11

arr = []

new = []

num = int(input("How many elements you want to insert: "))

for a in range(0,num):
    n = int(input("Enter the Numbers of elements: "))
    arr.append(n)

print("\nBefore removing the duplicate elements ftom the list... ")

print(arr)

print("\nAfter removing the duplicate elements ftom the list... ")

for i in arr:
    if i not in new:
        new.append(i)

print(new)



list1 = []
list2 = []

num1 = int(input("Enter the Number of elements for first list: "))

for i in range(1,num1+1):
    a = int(input("Enter the element: "))
    list1.append(a)

num2 = int(input("\nEnter the Number of elements for second list: "))

for i in range(1,num2+1):
    b = int(input("Enter the element: "))
    list2.append(b)


list3 = list1 + list2
list3.sort()

print("\n",list3)
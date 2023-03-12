# Practical no 3

import statistics
list = []
num = int(input("How many elements you want to insert: "))
for a in range(0,num):
    n = int(input("Enter the Numbers of elements: "))
    list.append(n)

print("\n",list,"\n")
print("The Average of the list is :",statistics.mean(list))






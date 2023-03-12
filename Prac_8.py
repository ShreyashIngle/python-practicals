# Practical No 8

values = int (input("Enter the value count: "))

n = []

for k in range(values):
    temp = int (input("Enter the interger value: "))
    n.append(temp)

for i in range(1,50):

    count = 0

    for j in n :
        if i%j == 0:
            count+=1
    
    else:
        if count == len(n):
            print(i,end=',')
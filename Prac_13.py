# Practical No 13

# Program1

# n = int(input("Enter the range: "))

start = 2

end = 100

# print("The Prime numbers between 1 - {0}: ".format(n))

for i in range(start,end+1):
    count = 0
    for j in range(2,i):
        if i%j ==0 :
            count ==1
            break
        
    if count==0:
        print(i)

m=int(input())
n=int(input())
for i in range(n):
    num=m
    row =""
    for j in range(1,n+1):
       row = row + str(num)+" "
       num = num + 1
    print(row)
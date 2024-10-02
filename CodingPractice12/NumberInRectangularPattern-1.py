m=int(input())
n=int(input())
for i in range(m):
    row=""
    for j in range(1,n+1):
        row = row + str(j)+" "
    print(row)
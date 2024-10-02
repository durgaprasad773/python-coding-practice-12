n=int(input())
factor = 0
for num in range(2,n):
    if n % num == 0:
        factor = factor + 1
        break
if factor == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")
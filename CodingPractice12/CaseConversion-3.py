s=input()
first = s[0].lower()
remain = s[1:]
res=""
for i in remain:
    if i.isupper():
        res = res + "-" + i.lower() 
    else:
        res = res + i
print(first+res)
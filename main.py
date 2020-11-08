a= int(input("Enter  number"))
b= int(input("Enter number"))
c= int(input("Enter number"))
if b<a :
    print(b)
elif c<b:
    print(c)
elif a<c :
    print(a)
print("Minimum number:",min(a,b,c))
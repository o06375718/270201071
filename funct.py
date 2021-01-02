a=[5,20,30,45,4]
sum=0
for i in range(len(a)):
        sum=sum+a[i]
print(sum)

def factoriel(item):
    if item==0:
        return 1
    else:
        return item*factoriel(item-1)
print(factoriel(5))



def reverse(s):
    reversed_s=""
    for i in s:
       reversed_s= i+ reversed_s
    print("Reversed string:",reversed_s)
s=input("Enter a string")
print("Entered string:",s)
reverse(s)
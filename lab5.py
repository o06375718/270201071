###### Multiplication Table ######
n=int(input("Enter a number:"))
for i in range(11):
  num=n*i
  print(str(n)+"x"+str(i)+"=",num)

###### Matching Digits #######
a=input("Enter a number:")
b=input("Enter a number:")
c=min(len(a),len(b))
num=[]
for i in range(-c,0):
  if a[i]==b[i]:
    num.append(i)
print(len(num))

####### % of evens ############
number=int(input("How many numbers?"))
list_num=[]
while number>0:
  num=int(input("Enter an integer:"))
  if num%2==0:
    list_num.append(num)
  number-=1
percent=float(len(list_num)*25)
print(str(percent)+" %")

######### Password Checker ###### 
password="abc123"
while True:
    a=input("Enter your password:")
    if a==password:
        print("Welcome")
        break
    elif a=="help":
        print(password[0])
    else:
        print("Wrong")

####### Fibonacci #######
a=0
b=1
n=int(input("Enter a number:"))
while n>0:
    a,b=b,a+b
    n=n-1
    print(a)

     
  


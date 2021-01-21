#### Absolute Value #####
num=int(input("Enter a number"))
if num<0:
  print(-num)
else:
  print(num)

##### Minimum Value #####
a=int(input("Enter a number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a<b:
  if c<a:
    print("Minimum value",c)
  else:
    print("Minimum value",a)
elif b<a:
  if c<b:
    print("Minimum value",c)
  else:
    print("Minimum value",b)


######## Graduation Condition #######
graduate=float(input("Enter your GPA:"))
lecture=int(input("Enter your number of the lectures:"))
if lecture<47  :
    if graduate<2.0:
        print("Not enough number of lectures and GPA")
    else:
        print("Not enough number of lectures")
else:
  if graduate<2.0:
    print("Not enough GPA!")
  else:
    print("GRADUATED!!!")

######### Ticket Discount ########
age=int(input("Enter your age:"))
ticket=3
if age<6 or age>60:
  print("Ticket is free")
elif 6<age<18:
  print("Ticket cost:",ticket*0.5)
else:
  print("Your ticket cost:",ticket)


###### Seasons #######
a=int(input("Enter day :"))
b=input("Enter aa month").capitalize()
if b=="March":
  if 20<a<=31:
    print("Spring")
  else:
    print("Winter")
elif b=="April" or "May":
    print("Spring")
elif  b=="June":
  if a<=20:
    print("Spring")
  else:
    print("Summer")
elif b=="July" or "August":
  print("Summer")
elif b=="September":
  if a<22:
    print("Summer")
  else:
    print("Fall")
elif b=="October" or "November":
  print("Fall")
elif b=="December":
  if a<21:
    print("Fall")
  else:
    print("Winter")
elif b=="January" or "February":
  print("Winter")

#####Roots of Quadratic Equation ######
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
diskriminant= (num2*num2)-4*num1*num3
if diskriminant>0:
  print("There are two real roots.")
elif diskriminant==0:
  print("There is one real root.")
else:
  print("There are two complex number.")
  
fac=1
x= int(input("Enter an number:"))
if x<0:
  print("Please enter an positive numbers")
elif x==0:
  fac=1
else:
      for i in range(1,x+1):
       fac=fac*i
print(fac)
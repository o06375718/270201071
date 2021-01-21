#### Sum of the last two digits #####
num=int(input("Enter a number:"))
a=num//10
b=num%10
print(a+b)

##### Leap year #####
year=int(input("Enter year:"))
if year%100==0:
    if year%4==0 and year%400==0:
        print("Leap year")
    else:
        print("Not Leap year ")
else:
    if year%4==0 and year%400==0:
        print("Leap year")
    else:
        print("Not Leap year ")
      
##### Sum of list #####
nums = [8, 60, 43, 55, 25, 134, 1]
sum=0
for i in nums:
  sum+=i
print(sum)

########## Power ############
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
power=1
while b>0:
    power=power*a
    b=b-1

print(power)


######## Factorial ########
n=int(input("Enter a number"))
factorial=1
while n>0:
  factorial=factorial*n
  n=n-1
print(factorial)

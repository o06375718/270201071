"""def sum_list(given_list):
  sum=0
  for i in given_list:
    sum+=i
  return sum**2
given_list=[12,-7,5,-89.4,3,27,56,57.3]
sum=sum_list(given_list)
"""

"""def is_prime_or_not(num1):
    count=0
    for i in range(2,num1):
      if num1%i==0:
        count=1
    if count==0:
       print("\n{} is a prime number".format(num1))
    else:
        print("\n{} is not a prime number".format(num1))

num1=int(input("\nEnter first number"))
is_prime_or_not(num1)

def print_prime_numbers_between(num2):
  for x in range(2,num2):
     if is_prime_or_not(x):
       print(x)

num2=int(input("Enter a second number"))
print_prime_numbers_between(num2)"""

"""
def is_prime(num1):
    count=0
    for i in range(2,num1):
      if num1%i==0:
        count=1
    if count==0:
       print("\n{} is a prime number".format(num1))

def print_prime_numbers_between(num2,num3):
  for y in range(num2,num3):
     if is_prime(y):
       print(y)

num3=int(input("\nEnter a third number"))
num4=int(input("\nEnter the last  number"))
print_prime_numbers_between(num3,num4)
"""


"""def is_prime_(n):
  if n<2:
    return False
  elif n==2:
    return True
  else:
    for i in range(2,n):
      if n%i==0:
        return False
    return True


n=int(input("Enter a number"))


for i in range(2,n):
  if is_prime_(i):
    print(i)"""

########GET OVERLAP#######
"""
import random
random.seed(123)

def get_random_list(b,e,N):
  r_list=random.sample(range(b,e),N)
  return r_list 
def get_overlap(L1,L2):
  L3=[]
  for num in L1:
    if num in L2:
      L3.append(num)
  return L3

def main():
  list1=get_random_list(b=0,e=10,N=5)
  list2=get_random_list(b=0,e=10,N=5)
  print(list1)
  print(list2)
  list3=get_overlap(list1,list2)
  print(list3)

main()
"""
def binary_to_dec(n):
  d=0
  get_reverse=str(n)[::-1]
  for i in range(len(get_reverse)):
     d=d+(2**i)*int(get_reverse[i])

  return d
print(binary_to_dec("100010"))

def dec_to_binary(d):
  b=""
  while d>0:
    b+=str(d%2)
    d=d//2
  return(b[::-1])
  
print(dec_to_binary(34))
#100010
#010001























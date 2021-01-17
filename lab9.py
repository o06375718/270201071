####### HARMONİC #########
def harmonic(n):
    if n==1:
        return 1
    else:
        return 1/n+ harmonic(n-1)
print(harmonic(5))

def iter_harmonic(n):
    sum=0
    for i in range(n):
        sum+=1/(i+1)
    return sum
a=iter_harmonic(5)
print(a)

####### REVERSE LİST ########
def get_reversed(my_list):#4,3,2,1    3,2,1   2,1  1
  if len(my_list)==0:
    return []
  else:
    return [my_list[-1]]+get_reversed(my_list[:-1])
                         # 4,3,2,1
                         #3,2,1
                         #2,1
                         #1
                         #[]
print(get_reversed([1,2,3,4,5]))

def get_reversed_second_option(my_list2):
  if len(my_list2)==0:
    return my_list2
  else:
    return [my_list2.pop()] +get_reversed_second_option(my_list2)

print(get_reversed_second_option([1,2,3,4,5]))


###### GET NUMBER OF EVENS ######
def number_evens(my_list):
  even=0
  for i in my_list:
      if i%2==0:
        even+=1
  return even

print(number_evens([0,1,2,3,4,5]))

def recursive_number_evens(list):#1,2,3,4,5,6
    if len(list)== 0:
        return 0
    counter=0
    if list[0]%2==0:#0 even mı bakıcak #1 even mı bakıcak
        counter=1
    return counter+ recursive_number_evens(list[1:])#
                            #1,2,3,4,5,6
                            #2,3,4,5,6
print(recursive_number_evens([0,1,2,3,4,5,6]))

####### SİMPLE TİMER #######
import time
def itr_sleep(t):
  for i in range(t,0,-1):
    print("Remaining time:",i)
    time.sleep(1)# print remaining time in each second

  print("Finish")

import time
def recursive_sleep(t):
  if t==0:
    print("Finish !")
  else:
    print("Remaining time:",t)
    time.sleep(1)  # print remaining time in each second
    return recursive_sleep(t-1) 
recursive_sleep(5)


number= int(input("Enter a number:"))
if number<10 :
   totals =number
else :
  ones= number %10 
  tens=( number//10)%10
  totals = ones +tens
  print("The sum of last two digit",totals)

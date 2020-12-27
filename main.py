travelling=int("Yes/No")
while travelling=="Yes":
   num=int(input("number of people travelling"))
   for travel in range(1,num+1):
      name=input("Please enter a name")

      age=input("Please enter age:")

      sex=input("Male/Female")

      print(name)

      print(age)

      print(sex)
      
travelling=input("Ooops Forgot someone")    
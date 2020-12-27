travelling=input("Yes/No")
while travelling=="Yes":
   num=int(input("number of travellers"))
   for i in range(1,num+1):
     name=input("Enter a name:")
     age=input("Enter an age:")
     sex=input("Male/Female")
    
     print(name)
     print(age)
     print(sex)
travelling=input("Ooops,You forgot someone")
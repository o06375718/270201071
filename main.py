age= int(input("How old are you?"))
ticket=3
if age<6 and age>60:
    print("Your ticket is free")
elif  6<= age <= 18 :
    print("Your ticket cost:",ticket/2)
else  :
    print("Your ticket cost:",3) 
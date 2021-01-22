######### Print the names ##############
name_age=[("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]
for x in name_age:
    if x[1]>18:
        print(x[0])
########### Books #########
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict={}
book_dict_3={}
for i in books:
  a=len(i)
  b=""
  for j in i :
    if j not in b:
        b+=j
  c=len(b)
  book_dict[i]=(a,c)
  book_dict_3[i]=(a,c,(a+c)//2) # Books (cont.)

print(book_dict)
print(book_dict_3)

######### Employee ###########
for i in range(5):
  employees={}
  print("Employee"+i)
  employee=input("Enter a name:")
  salary=int(input("Enter a salary:"))
  employees[i]=salary


  
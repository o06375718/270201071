###### Non-trivial String Comparasion ######
email=input("Email adress:").lower()
def check(email):
  if email=="ceng113@example.com":
      return True
  elif email=="c.e.n.g113@example.com":
      return True
print(check(email))
email = input("Please enter an email address:")

ref_mail = "ceng113@example.com"

if "@" in email: 
  email = email.lower()
  part_1 = email.split("@")[0]
  part_1 = part_1.replace(".", "")
  part_2 = email.split("@")[1]
  email = part_1 + "@" + part_2
  print(email)
  if email == ref_mail:
     print("Equal")
  else:
     print("Not equal")
else:
  print("Not equal")

####### Average Grades #########
grade_list = []
n_st = int(input("Please enter number of students:"))
for i in range(n_st):
  print("Student ", str(i+1))
mid_1 = int(input("Midterm 1:"))
mid_2 = int(input("Midterm 2:"))
f_grade = int(input("Final:"))
grade_list.append([mid_1,mid_2,f_grade])
print(grade_list)
avg_grades = []
for sub_grades in grade_list:
  avg_grades.append(sub_grades[0]*0.3 + sub_grades[1]*0.3 + sub_grades[2]*0.4)
print(avg_grades)

######## Finding AA Students (cont.)​ #########
greater_90=[]
for i in avg_grades:
    if i>90 :
        greater_90.append(i)
print(greater_90)

######## Unique List​ #######
number=int(input("The number of items:"))
num_list=[]
final_list=[]
for i in range(number):
    num=int(input("Enter a number:"))
    num_list.append([num])
for i in num_list:
    if i not in final_list:
        final_list.append(i)

print(final_list)
####### Identity Matrix ########
def identity(n):
    m=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        m[i][i] = 1
    return m
print(identity(3))

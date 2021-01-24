######## Cylinder #########
import math
class Cylinder:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def get_radius(self):
        return self.radius
    def set_radius(self,radius):
        if radius>0:
             self.radius=radius
    def get_height(self):
        return self.height
    def set_height(self, height):
         if height>0:
             self.height = height
    def basearea(self):
        return math.pi*(self.radius**2)
    def surfacearea(self):
        return 2*(math.pi*self.radius)*self.height
    def area(self):
        return 2*(self.basearea())+(self.surfacearea())
    def volume(self):
        return self.basearea()*self.height
cylinder1=Cylinder(radius=3,height=5)
print(cylinder1.area())
print(cylinder1.volume())

############### Employee ########
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_salary(self):
        return self.salary
    def set_salary(self,salary):
        self.salary=salary
    def display(self):
        print("Name:"+str(self.name))
        print("Salary:"+str(self.salary))

class Company:
    def __init__(self):
        self.employee_list=[]
    def get_list_employee(self):
        return self.employee_list
    def set_list_employee(self,current_list):
        if type(current_list)==list:
            self.employee_list=current_list
    def add_employee(self,new_employee):
        if isinstance(new_employee,Employee):
            self.employee_list.append(new_employee)
    def calc_average_salary(self):
        total_sum=0
        for emp in self.employee_list():
            total_sum+=emp.get_salary()
        return total_sum/len(self.employee_list)

    def display(self):
        for emp in self.employee_list():
            print("Name :"+str(self.get_name()))
            print("Salary:"+str(self.get_salary()))
c=Company([])
e1=Employee("Merve",10000)
e2=Employee("Sefa",12000)
e3=Employee("Hülya",100000)
c.add_employee(e1)
c.add_employee(e2)
c.add_employee(e3)
#c.add_employee("90") if  we write this employee de tanımlanmadığı için kabul edilmez
#c.add_employee(90)
c.display()




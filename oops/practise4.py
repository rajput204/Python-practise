#instaance and class variable
class Employee:
    empolyee_count=101
    def __init__(self,name,salary,designation):
        self.name=name
        self.salary=salary
        self.designation=designation
        self.eid='e'+str(Employee.empolyee_count)
        Employee.empolyee_count+=1
    def show_details(self):
        print('name',self.name)
        print('salary',self.salary)
        print('designation',self.designation)
        print(self.eid)
    @classmethod
    def employeecount(cls):
        return cls.empolyee_count
e=Employee("aditya",105000,"ceo")
e.show_details()
print(Employee.employeecount())
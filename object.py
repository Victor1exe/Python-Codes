'''class Employee:
    company="Google"
    def name(self):
        self.name="name"
    def getsalary(self):
        print(f"Salary for {self.name} in {self.company} is {self.salary}")
victor=Employee()
victor.name="Victor"
victor.salary=100000
victor.getsalary()'''

'''class Employee:
    company="Brs"
    def name(self):
        self.name="name"
    def salary(self):
        self.salary="salary"
    def getdetails(self):
        print(f"The salary of {self.name} working in {self.company} is {self.salary}")     
    @staticmethod
    def greet():
        print(f"Hello")

victor=Employee()
victor.name="Victor"
victor.salary="100000"
Employee.company="Ld"
victor.greet()  #whatever the order be the static will be printed first
victor.getdetails()'''

'''class Employee:
    def __init__(self,name,salary,company,subunit):
        self.name=name
        self.salary=salary
        self.company=company  #here don,t use the double or single inverted commas
        self.subunit=subunit
    def getdetails(self):
        print(f"The salary of {self.name} is {self.salary}")
        print(f"The company of {self.name} is {self.company}")
        print(f"The subunit of {self.name} is {self.subunit}")
 
victor=Employee("Victor","100000","Youtube","DBA")
victor.getdetails()'''





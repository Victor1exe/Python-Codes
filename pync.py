#classes 
class Empl():
    task="Assassination"
    salary="$40000"
    rank="XYZ"
    bonus="$3000"
    name="ABC"

    def __init__(self,name,rank,task,salary,bonus):
        self.name=name
        self.task=task
        self.salary=salary
        self.rank=rank
        self.bonus=bonus

    def get_details(self):
        print(f"The name of empl is:\t{self.name}")    
        print(f"The rank of empl is:\t{self.rank}")      
        print(f"The task of empl is:\t{self.task}")  
        print(f"The salary of empl is:\t{self.salary}")  
        print(f"The bonus gained by empl is:\t{self.bonus}")  

#object
a=Empl("Thug_01","Bomb squad","22 Bombs Deployment","$40000","$1500")
a.get_details()

b=Empl("Thug_01","Bomb squad","22 Bombs Deployment","$1500")
b.get_details()


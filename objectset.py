'''class Employees:
    company="Microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getdetails(self):
        print(f"The employee {self.name} of {self.company} has a salary of {self.salary}")
victor=Employees("Victor","$5000")
victor.getdetails()
sumedha=Employees("Sumedha","$8000")
sumedha.getdetails()'''



'''class Calculator:
    def sqr(self):
        print(f"The square of the number is", number**2)
    def sqr_rt(self):
        print(f"The square root of the number is",number**1/2)
    def cube(self):
        print(f"The cube of the number is",number**3)
    @staticmethod
    def greet():
        print("Hello")
    
number=int(input("Enter the number"))
num=Calculator()
num.sqr()
num.greet()
num.sqr_rt()
num.cube()'''


print("Welcome to the Indian Railways.")

class TrainBooking:
    railway_org="Indian Railways"
    def status(self):
        print("The number of seats available in the Train is 80.\n Available for booking.")
    def book(self):
        print("The number of seats you want to book is", seats )
        print("Proceeding to the payment page.")
    def fare(self):
        print("Cost per head is Rs400")
        if(seats<=3):
            print("Your Fare is ", seats*400)
        elif((seats>3) & (seats<=8)):
            print(f"You will get a discount of 20% on the bookings.")
            print("Your Fare is ", seats*400-seats*400*.2)
        else:
            print(f"You will get a discount of 35% on the bookings.")
            print("Your Fare is ", seats*400-seats*400*.35)
    def greet(self):
        print(f"Thanks for choosing {self.railway_org}")

seats=int(input("Enter the number of seats to be reserved:"))
bookings=TrainBooking()
bookings.status()
bookings.book()
bookings.fare()
bookings.greet()
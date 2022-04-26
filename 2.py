
class Person:
    country = "india"
    def __init__(self):
        print("Initialising Person......")
    def takeBreath(self):
        print("I'm breathing......")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initialising Employee")
    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so I am Breathing...")

e = Employee()
e.takeBreath()

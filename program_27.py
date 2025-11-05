'''
OOP Concepts
'''

class Employee:
    name = "Nirav"
    language = "Python"
    salary = 1500000
    def __init__(self): #this is the Dunder Method, which is call automatically
        print("I am Creating a Object")
        
    def getInfo(self):
        print(f"Employee Name is {self.name} and he is working on {self.language} and his salary is {self.salary}")

    @staticmethod #with this there is no need to write the self in the function
    def greet():
        print("Good Morning Everyone")

nirav = Employee()
nirav.greet()
nirav.getInfo()
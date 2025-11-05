'''
OOP Concepts
'''

class Employee:
    def __init__(self, name, language, salary): #this is the Dunder Method, which is call automatically
        self.name = name
        self.language = language
        self.salary = salary
        print("I am Creating a Object")
        
    def getInfo(self):
        print(f"Employee Name is {self.name} and he is working on {self.language} and his salary is {self.salary}")

    @staticmethod #with this there is no need to write the self in the function
    def greet():
        print("Good Morning Everyone")

nirav = Employee("Nirav","Python",1500000)
nirav.greet()
nirav.getInfo()
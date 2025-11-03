# Function
def avg():
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    c = int(input("Enter Number 3: "))

    avg = (a+b+c)/3
    print(avg)

avg()

def greetPerson(name1):
    print(f"Good Day {name1}")

greetPerson("Nirav")
greetPerson("Raj")
greetPerson("Mohan")

# Recursion
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a Number: "))
print(f"The Factorial of the Number {n} is {factorial(n)}")

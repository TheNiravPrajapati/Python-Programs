n = int(input("Enter the Number: "))

# Table of Number
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")

print("")
# Table of Number in reverse
for i in range(1, 11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")

# Prime or not 
for i in range(2, n):
    if(n%i) == 0:
        print("Number is Not Prime")
        break
else:
    print("This is Prime Number")

# Factorial of Number
fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f"factorial of {n} is {fact}")
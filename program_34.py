# Exception Handling 
try:
    a = int(input("Enter a Number: "))
    print(f"The Entered Number is {a}")

except ValueError as v:
    print("Enter valid Number")
    
except Exception as e:
    print(e)

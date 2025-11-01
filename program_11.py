a1 = int(input("Enter Number 1: "))
a2 = int(input("Enter Number 2: "))
a3 = int(input("Enter Number 3: "))
a4 = int(input("Enter Number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("NO 1 is Greater, No. is ", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("No 2 is Greater, No. is ", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("No 3 is Greater, No. is ", a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("No 4 is Greater, No. is ", a4)
else:
    print("Invalid Number")
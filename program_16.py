'''
For This Patten
    N
   NNN
  NNNNN
 NNNNNNN
NNNNNNNNN
'''
n = int(input("Enter Number: "))
character = input("Enter Character: ")
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print(f"{character}" * (2 * i - 1), end="")
    print("")

'''
For this Patten
***
* *
***
'''
n2 = int(input("Enter Number: "))
for i in range(1, n2+1):
    if(i ==1 or i ==n2):
        print("*" * n2, end="")
    else:
        print("*", end="")
        print(" " * (n2-2), end="")
        print("*", end="")
    print("")

import random

n = random.randint(1, 100)
a = -1
gueses = 0
while(a != n):
    a = int(input("Guess The Number: "))
    if(a>n):
        print("Lower Number Please")
        gueses += 1
    elif(a<n):
        print("Higher Number Plesase")
        gueses += 1

print(f"You Have Gussed the Number {n} in {gueses} Attempts")
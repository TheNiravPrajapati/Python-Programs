import random
import time
from termcolor import colored

# Fancy intro
print(colored("\n🐍🐍🐍  WELCOME TO SNAKE WATER GUN GAME  🐍🐍🐍", "cyan", attrs=["bold"]))
print(colored("Rules:", "yellow"))
print("1️⃣ Snake drinks Water → Snake wins 🐍")
print("2️⃣ Gun kills Snake → Gun wins 🔫")
print("3️⃣ Water damages Gun → Water wins 💧")
print("Let's Play!\n")

# Mapping
choices = {"s": 1, "w": -1, "g": 0}
reverse_choices = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

user_score = 0
computer_score = 0
rounds = int(input("How many rounds do you want to play? 🎯 "))

for i in range(1, rounds + 1):
    print(colored(f"\nRound {i} 🔥", "magenta", attrs=["bold"]))
    user_input = input("Choose (s for Snake, w for Water, g for Gun): ").lower()

    if user_input not in choices:
        print(colored("Invalid choice! Try again 😅", "red"))
        continue

    you = choices[user_input]
    computer = random.choice([-1, 0, 1])

    print(colored("\nComputer is choosing...", "yellow"))
    time.sleep(1)
    print(f"Computer chose: {reverse_choices[computer]}")
    print(f"You chose: {reverse_choices[you]}")

    # Decision logic
    if computer == you:
        print(colored("It's a DRAW 🤝", "cyan"))
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print(colored("🎉 You WIN this round!", "green", attrs=["bold"]))
        user_score += 1
    else:
        print(colored("💀 You LOSE this round!", "red", attrs=["bold"]))
        computer_score += 1

    print(colored(f"Score -> You: {user_score} | Computer: {computer_score}", "yellow"))

# Final Results
print(colored("\n🏁 GAME OVER 🏁", "cyan", attrs=["bold"]))
if user_score > computer_score:
    print(colored("🎊 Congratulations! YOU WON THE GAME! 🏆", "green", attrs=["bold"]))
elif user_score < computer_score:
    print(colored("😢 Oh no! The COMPUTER WON! 🤖", "red", attrs=["bold"]))
else:
    print(colored("😮 It's a TIE! Well played!", "blue", attrs=["bold"]))

print(colored(f"Final Score -> You: {user_score} | Computer: {computer_score}", "yellow"))
print(colored("\nThanks for playing Snake-Water-Gun! 👋", "cyan", attrs=["bold"]))

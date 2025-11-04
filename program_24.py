import random
def game():
    print("You are Playing the Amazing Game")
    score = random.randint(1, 62)
    with open("Files/highScore.txt") as f:
        highScore = f.read()
        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0
    print(f"Your Score: {score}")
    if(score>highScore or highScore == ""):
        with open("Files/highScore.txt", "w") as f:
            f.write(str(score))

    return score

game()

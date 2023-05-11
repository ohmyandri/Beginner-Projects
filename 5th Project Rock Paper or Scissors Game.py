import random


def getChoices():
    gameOptions = ["Rock", "Paper", "Scissors"]
    playerChoice = input("Enter a choice between Rock Paper or Scissor: ")
    computerChoice = random.choice(gameOptions)
    choices = {"Player": playerChoice, "Computer": computerChoice}
    return choices


def checkWin(Player, Computer):
    print(f"You chose {Player} and Computer chose {Computer}")
    if Player == Computer:
        return "It's a tie"

    elif Player == "Rock":
        if Computer == "Scissors":
            return "Rock smashes scissors, You Win!"
        else:
            return "Paper covers Rock, Computer Win!"

    elif Player == "Paper":
        if Computer == "Rock":
            return "Paper covers Rock, You Win!"
        else:
            return "Scissors cut Paper, Computer Win!"

    elif Player == "Scissors":
        if Computer == "Paper":
            return "Scissors cut Paper, You Win!!"
        else:
            return "Rock smashes scissors, Computer Win!"


choices = getChoices()
result = checkWin(choices["Player"], choices["Computer"])
print(result)
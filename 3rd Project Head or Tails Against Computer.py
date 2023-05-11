import random

def selector():
    print("Welcome to The Coin Flipper code!")
    computerChoice = random.choice(["HEAD", "TAILS"])
    userChoice = input("What do you Choose, Head or Tails?: ").upper()
    coinFlip = random.choice(["HEAD", "TAILS"])

    if computerChoice == coinFlip:
        return f"You Lose by selecting {userChoice}! and The computer Wins!, The coin actually flipped on {coinFlip}!"

    elif userChoice == coinFlip:
        return f"The Computer Lose by selecting {computerChoice} The User Wins!, The coin flipped on {coinFlip}!"

    elif userChoice and computerChoice == coinFlip:
        return f"Both Players were right, The Coin Flipped on {coinFlip}!"

    elif userChoice and computerChoice != coinFlip:
        return f"Both Players were wrong, The Coin actually Flipped on {coinFlip}!"

print(selector())
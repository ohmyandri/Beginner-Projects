#WE USE THIS TO IMPORT THE RANDOMIZER SELECTOR
from random import choice

series = ["The Walking Dead", "Breaking Bad", "Rick and Morty"]
animes = ["Blue Lock", "Naruto", "Vagabond", "Your lie in Apri"]
print("Welcome to the Anime and Series Selector")
selector = input("What do you want to watch, (A)nime or (S)eries: ")

if selector.upper() == "A":
    print("Then you should watch: " + choice(animes))

elif selector.upper() == "S":
    print("Then you should watch: " + choice(series))

else:
    print("Sorry, that's not an option")


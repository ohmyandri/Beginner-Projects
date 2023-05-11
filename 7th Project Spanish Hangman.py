import random
from wordslib import spanishWords
import string


def validWord(spanishWords):
    randomWord = random.choice(spanishWords)

    return randomWord.upper()

#Once defined our words, the hangman game will start

def hangman():
    randomWord = validWord(spanishWords)
    separateLetter = set(randomWord)
    alphabet = set(string.ascii_uppercase) #We'll select the alphabet on upper case so all of the words display on uppercase letters
    lettersUsed = set()

    #We also want our game, not to be so easy, so we'll make that we can only fail our letter to guess, 5 times
    lives = 5

    #first we'll tell the user how many lives does he have, and wich letters has he already guessed
    while len(separateLetter) > 0 and lives > 0:
        print("Tienes ", lives, "vidas, Y has usado las siguientes letras: ", " ".join(lettersUsed))
        #we'll make the letters that he use enter to the lettersUsed variable, and storage them right in there

    #I'll also will tell the player how the word looks, and how many letters is this word
        correctWords = [letter if letter in lettersUsed else "-" for letter in randomWord]
        print("La palabra se ve de la siguiente manera: ", " ".join(correctWords))

        userElection = input("Elige una letra para empezar: ").upper() #We need the user input to be uppercased so it match with the alphabet and word Uppercased Format
        if userElection in alphabet - lettersUsed: #If the letter guessed from the user isnt on the letter separed on the word or at the alphabet, we'll quit that word, so the user stop guessing it
            lettersUsed.add(userElection)
            if userElection in separateLetter:
                separateLetter.remove(userElection)

            else:
                lives = lives - 1
                print("La letra que elegiste no es parte de esta palabra")

        elif userElection in lettersUsed:
            print("Ya has elegido esta letra")

        else:
            print("Has escogido un caracter incompatible, trata de nuevo!")


    #End Of The Game, Now we gotta end the game, and for this, we can end the game in two situations, if the player guess the word, or the player ends without any single live

    if lives == 0:
        print("Has perdido! no te queda ninguna vida, La Palabra era: ", randomWord)
    else:
        print("Has ganado!, La palabra correcta era: ", randomWord)


hangman()
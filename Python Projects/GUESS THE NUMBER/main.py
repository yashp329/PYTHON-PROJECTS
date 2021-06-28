import random
randNumber = random.randint(1,100)
guesses = 0
userGuess = None

while(userGuess != randNumber):
    userGuess = int(input('Enter your guess :'))
    guesses +=1
    if(userGuess == randNumber):
        print("You guessed it correctly!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong ! Enter a smaller number")
        else:
            print("You guessed it wrong ! Enter a larger number")
    

print(f"You guessed the number in {guesses} guesses")           


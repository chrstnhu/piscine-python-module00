import sys
import random

def printRules() :
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")

def guessGame(secretNumber) :
    
    attempts = 1
    while True:
        print("What's your guess between 1 and 99?")
        number = input(">> ")
        # Exit programm
        if (number == "exit"):
            print("Goodbye!")
            break
        
        # Check the number
        if (number.isdigit()):
            if int(number) == secretNumber:
                if (secretNumber == 42) :
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                if (attempts == 1) :
                    print("Congratulations! You got it on your first try!")
                else :
                    print("Congratulations, you've got it!")
                    print(f"You won in {attempts} attempts!")
                break
            elif int(number) > secretNumber:
                print("Too high!")
                attempts += 1
            else :
                print("Too low!")
                attempts += 1
        else :
            print("That's not a number.")

# Main
if __name__ == "__main__":
    printRules()

    secretNumber = random.randint(1, 99)
    guessGame(secretNumber)


        
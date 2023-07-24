import random

print("Hi there! I'm Nicolae Alexandru Badea and I want to play a fun game with you")
print("The rules are simple. I'm thinking of a number between 1 and 100 and you should guess it")
print("I will tell you if you are getting warmer or colder")
print("Let's start!")

def guess_number():
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Type your guess here: "))
        attempts += 1

        if guess == random_number:
            print("------------<<<<<<<<< YOU GUESSED IT! >>>>>>>>>>>>>-----------------")
            print(f"You guessed it! Congratulations!")
            print("-------------------<<<<<<<<< GAME OVER >>>>>>>>>>>>>-----------------")
            print("Number of attempts:", attempts)
            break
        elif abs(guess - random_number) <= 5:
            print("-------------------<<<<<<<<< HOT >>>>>>>>>>>>>-----------------")
        elif abs(guess - random_number) <= 10:
            print("-------------------<<<<<<<<< WARM >>>>>>>>>>>>>-----------------")
        else:
            print("-------------------<<<<<<<<< COLD >>>>>>>>>>>>>-----------------")

    play_again = input("-------------------<<<<<<<<< PLAY AGAIN? >>>>>>>>>>>>>-----------------")
    

    if play_again.lower() == "yes":
        guess_number()
    else:
        print("Thank you for playing!")
        exit()
guess_number()

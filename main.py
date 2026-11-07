#NUMBER GUESSING GAME

#importing the random module
import random

# function to guess number
def number_guessing():
    number = random.randint(1, 100)
    attempts = 0

    print("\n---- NUMBER GUESSING GAME ----")
    print("I have chosen a random number")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if attempts==5:
                if number%2==0:
                    print("\n Hint:It is an even number:")
                else:
                    print("\n Hint:It is an odd number")
            if guess > number:
                print("Too high")
            elif guess < number:
                print("Too low")
            else:
                print("Correct!")
                print(f"You guessed it in {attempts} attempts.")
                print("Game Over!")
                break

        except ValueError:
            print("Invalid guess! Try again.")


# function to play again
def play_again():
       while True:
           answer = input("Do you want to play again? (yes/no): ").lower()
           if answer == "yes":
               number_guessing()
           else:
               print("Thanks for playing!")


number_guessing()
play_again()      
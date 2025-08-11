import random


def magic_number_game():
    magic_number = random.randint(1, 100)
    print("🔮 Welcome to the Magic Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < magic_number:
                print("Too low! 📉 Try again.")
            elif guess > magic_number:
                print("Too high! 📈 Try again.")
            else:
                print(
                    f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")


# Run the game
magic_number_game()

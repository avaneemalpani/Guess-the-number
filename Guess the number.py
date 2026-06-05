import os
import platform

def play_game():
    print("\n Welcome to Guess the Number!")

    
    number=int(input("Enter number to guess:"))
    input("Press Enter to start the game...")
    os.system('cls' if os.name == 'nt' else 'clear')

    max_attempts=3
    attempts=0
    

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess:"))
            attempts += 1

            if guess < number:
                print("Too low ⬇")
            elif guess > number:
                print("Too high ⬆")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                return

        except ValueError:
            print("Please enter a valid number!")

        print(f"Attempts left: {max_attempts - attempts}")

    print(f"\nYou lost! The number was {number}.")

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

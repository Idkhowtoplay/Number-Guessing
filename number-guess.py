import argparse
import random

def main():
    parser = argparse.ArgumentParser(description="number guess")
    subparsers = parser.add_subparsers(dest="command")

    guess = subparsers.add_parser('start', help="start game")
    args = parser.parse_args()
    if args.command == "start":
        start()

def start():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("You have 5 chances to guess the correct number")
    
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. medium (5 chances)")
    print("3. Hard (3 chances)")
    print()

    diff = int(input("Enter your choice:"))
    if diff > 3 or diff < 1:
        print("Invalid number")
    else:
        message = {
            1: "Great! You have selected the easy level.",
            2: "Great! You have selected the medium level.",
            3: "Great! You have selected the hard level"
        }
        print(message[diff])
        print("Let's start the game!")
        game(diff)

def game(diff):
    count = 0
    number = random.randint(1, 100)
    chances_by_diff = {1: 10, 2: 5, 3: 3}
    chances = chances_by_diff.get(diff, 10)

    while True:
        guess = int(input("Enter you guess:"))
        if count == chances:
            print(f"Game over the number is {number}")
            break

        if guess > number:
            print(f"Incorrect The number is less than {guess}")
            count += 1
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}")
            count += 1
        else:
            print(f"Congratulation! You guessed the correct number in {count} attempts")
            break

main()
# A Hangman Game that lets users guess a random word in max 6 tries

# Importing random module + custom word list
import random
from wordlist import words

# Dictionary that forms Hangman Art based on wrong guesses
hangman_art = {0 : ("   ",
                    "   ",
                    "   "),
               1 : (" o ",
                    "   ",
                    "   "),
               2 : (" o ",
                    " | ",
                    "   "),
               3 : (" o ",
                    "/| ",
                    "   "),
               4 : (" o ",
                    "/|\\",
                    "   "),
               5 : (" o ",
                    "/|\\",
                    "/  "),
               6 : (" o ",
                    "/|\\",
                    "/ \\")}

# Function displays hangman art
def display_hangman(wrong_guesses):
    print("*********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*********")

# Function displays hint (Where the guessed letter is)
def display_hint(hint):
    print(" ".join(hint))

# Function displays answer (For end of game)
def display_answer(answer):
    print(" ".join(answer))

# Main game loop
def main():
    answer = random.choice(words)    # Answer becomes a random word from our module
    hint = ["_"] * len(answer)       # Hint's length is defined by word choice
    wrong_guesses = 0                # User starts with 0 wrong guesses
    guessed_letters = set()          # Creates a set for User guesses
    is_running = True

    print("Welcome to Hangman!")
    print("-------------------")

# Main while loop
    while is_running:
        display_hangman(wrong_guesses)     # Prints the hangman artwork
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        # Catches Error if guess != 1 letter or != alpha
        if len(guess) < 1 or len(guess) > 1 or not guess.isalpha():
            print("Invalid. Please enter 1 letter.")
            continue

        # Catches if letter has already been guessed
        if guess in guessed_letters:
            print(f"{guess.capitalize()} is already guessed! ")
            continue

        guessed_letters.add(guess)      # Adds guess to guessed_letters

        # Switches "_" for guess in Hint
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1   # Adds a wrong guess

        # Prints "YOU WIN" once User guesses correct word
        if "_" not in hint:
            display_hangman(wrong_guesses)    # Displays hangman artwork
            print(f"Correct Answer: {answer}")
            print("YOU WIN!")
            is_running = False  # Ends the program

        # Prints "YOU LOSE" once User runs out of guesses
        elif wrong_guesses >= 6:
            display_hangman(wrong_guesses)    # Displays hangman artwork
            print(f"Correct Answer: {answer}")
            print("YOU LOSE...")
            is_running = False  # Ends the program

# Activates main()
if __name__ == "__main__":
    main()
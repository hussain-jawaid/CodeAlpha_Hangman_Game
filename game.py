import random
from words import words_list


def get_hangman_art():
    """Return the visual stages of the hangman."""
    return [
        """
        +---+
        |   |
            |
            |
            |
            |
    =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
    =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
    =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
    =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    =========
        """
    ]


def get_random_word():
    """Select a random word from the list and return it in uppercase."""
    return random.choice(words_list).upper()


def initialize_game(word):
    """Set up initial game state and display introductory messages."""
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("\nLet's Play Hangman!")
    print(f"\nWord: {' '.join(guessed_word)} ({len(word)} letters)")
    print(f"Attempts remaining: {attempts}")
    return guessed_word, guessed_letters, attempts


def play_game(word):
    """Manage the main game logic and user interactions."""
    guessed_word, guessed_letters, attempts = initialize_game(word)
    hangman_pics = get_hangman_art()
    print(hangman_pics[6 - attempts])

    while attempts > 0:
        guess = input("\nEnter a letter: ").strip().upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already tried that letter. Try another one!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect guess! Attempts remaining: {attempts}")
            print(hangman_pics[6 - attempts])
            if attempts == 0:
                print(f"\nGame over! The word was: {word}")
                return
        else:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            if "_" not in guessed_word:
                print("\nCongratulations! You won!")
                print(f"The word was: {' '.join(guessed_word)}")
                return

        print(f"\nWord progress: {' '.join(guessed_word)}")


def main():
    """Control the game flow and restart functionality."""
    while True:
        secret_word = get_random_word()
        play_game(secret_word)
        
        replay = input("\nPlay again? (Y/N): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
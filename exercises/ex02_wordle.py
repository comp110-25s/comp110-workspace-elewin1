"""Wordle exercise!"""

__author__ = "730521441"


def contains_char(word: str, letter: str) -> bool:
    """Checks if letter is in word"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1
    return False


# contains_char is used to check if a each letter in the guessed work is found within the secret word


def emojified(guess: str, secret: str) -> str:
    """determines what color box to print based on guessed letter"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i = 0
    box = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            box += GREEN_BOX
        elif contains_char(word=secret, letter=guess[i]):
            box += YELLOW_BOX
        else:
            box += WHITE_BOX
        i += 1
    return box


# emojififed is what prints the boxes of green, yellow, and white based off the character guessed


def input_guess(length: int) -> str:
    """determines if length of guessed word == length of secret word"""
    N = length
    word: str = input(f"Enter a {N} character word:")
    while len(word) != length:
        word = input(f"That wasn't {length} chars! Try again:")
    return word


# imput_guess determines if guessed word is equal to length of secret word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_guesses: int = 6
    turn: int = 1
    won: bool = False

    while turn <= max_guesses and not won:
        print(f"=== Turn {turn}/{max_guesses} ===")
        guess: str = input_guess(len(secret))
        emojified(guess, secret)

        if guess == secret:
            won = True
            print((f"You won in {turn}/{max_guesses} turns!"))
        else:
            turn += 1
    if not won:
        print(f"X/{max_guesses} - Sorry, try again tomorrow!")


# main function brings all the other functions together to make the game

if __name__ == "__main__":
    main(secret="codes")

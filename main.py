MAX_WORD_LENGTH = 11
MIN_WORD_LENGTH = 5

def start():
    """
    function that starts the hangman game
    """

    word = input("Please enter the word to be guessed: ")
    while ( len(word) < MIN_WORD_LENGTH ) or ( len(word) > MAX_WORD_LENGTH ):
        word = input("Word too long, enter again")

    game_end = False
    guess_letter = ""
    while not game_end:
        while
        guess_letter = input("Guess the next letter")


if __name__ == "__main__":
    start()
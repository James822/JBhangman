MAX_WORD_LENGTH = 11
MIN_WORD_LENGTH = 5

def gui(w):
    print("\t\t______________")
    print("\t\t|             |")
    print("\t\t|             |")
    print("\t\t              |")
    print("\t\t              |")
    print("\t\t              |")
    print("\t\t              |")
    print("\t\t              |")
    print("\t\t              |")
    print("\t\t              |")
    print("\t\t           _______")
    for n in range(len(w)):
        print("_ ", end="")

    print("\n")
    
def start():
    """
    function that starts the hangman game
    """

    word = input("Please enter the word to be guessed: ")
    while ( len(word) < MIN_WORD_LENGTH ) or ( len(word) > MAX_WORD_LENGTH ):
        word = input("Word too long, enter again")

    game_end = False
    guess_letter = ""
    while not game_end: #while game is running
        gui(word)
        guess_letter = input("Guess the next letter: ") # Guess a letter
        for charnum in range(len(word)): #for each letter in the word
            if guess_letter == word[charnum]:
                print("This letter exists in the word @pos: ")
                
                print(charnum)        

if __name__ == "__main__":
    start()

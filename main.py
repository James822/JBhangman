MAX_WORD_LENGTH = 11
MIN_WORD_LENGTH = 5

def gui(word, found_list, guesss_list, hang_state):
    if hang_state == 0:
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
        for n in range(len(word)):
            if found_list[n] != "":
                print (found_list[n] + " ", end="")
            else:
                print("_ ", end="")
        print("\n")
        return False
    if hang_state == 1:
        print("\t\t______________")
        print("\t\t|             |")
        print("\t\t|             |")
        print("\t\t0             |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t           _______")
        for n in range(len(word)):
            if found_list[n] != "":
                print (found_list[n] + " ", end="")
            else:
                print("_ ", end="")
        print("\n")
        return False
    if hang_state == 2:
        print("\t\t______________")
        print("\t\t|             |")
        print("\t\t|             |")
        print("\t\t0             |")
        print("\t\t|             |")
        print("\t\t|             |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t           _______")
        for n in range(len(word)):
            if found_list[n] != "":
                print (found_list[n] + " ", end="")
            else:
                print("_ ", end="")
        print("\n")
        return False
    if hang_state == 3:
        print("\t\t______________")
        print("\t\t|             |")
        print("\t\t|             |")
        print("\t\t0             |")
        print("\t      --|             |")
        print("\t\t|             |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t           _______")
        for n in range(len(word)):
            if found_list[n] != "":
                print (found_list[n] + " ", end="")
            else:
                print("_ ", end="")
        print("\n")
        return False
    if hang_state == 4:
        print("\t\t______________")
        print("\t\t|             |")
        print("\t\t|             |")
        print("\t\t0             |")
        print("\t      --|--           |")
        print("\t\t|             |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t           _______")
        for n in range(len(word)):
            if found_list[n] != "":
                print (found_list[n] + " ", end="")
            else:
                print("_ ", end="")
        print("\n")
        return False
    if hang_state == 5:
        print("\t\t______________")
        print("\t\t|             |")
        print("\t\t|             |")
        print("\t\t0             |")
        print("\t      --|--           |")
        print("\t\t|             |")
        print("\t       /              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t           _______")
        for n in range(len(word)):
            if found_list[n] != "":
                print (found_list[n] + " ", end="")
            else:
                print("_ ", end="")
        print("\n")
        return False
    if hang_state == 6:
        print("\t\t______________")
        print("\t\t|             |")
        print("\t\t|             |")
        print("\t\t0             |")
        print("\t      --|--           |")
        print("\t\t|             |")
        print("\t       / \            |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t              |")
        print("\t\t           _______")
        for n in range(len(word)):
            if found_list[n] != "":
                print (found_list[n] + " ", end="")
            else:
                print("_ ", end="")
        print("\n")      
        print("YOU LOSE! BETTER LUCK NEXT TIME!")
        return True
    
    
def start():
    """
    function that starts the hangman game
    """

    word = input("Please enter the word to be guessed: ").lower()
    while ( len(word) < MIN_WORD_LENGTH ) or ( len(word) > MAX_WORD_LENGTH ):
        word = input("Error, word must be > 5 and < 11 letters. Enter again: ").lower()

    game_end = False
    guess_letter = ""
    found_list = [""] * len(word) # correct guesses
    guess_list = [] # failed guesses (all other guesses)
    hang_state = 0
    while not game_end: #while game is running
        game_end = gui(word,found_list, guess_list, hang_state)
        if game_end == False:
            guess_letter = input("Guess the next letter: ").lower() # Guess a letter
            while(len(guess_letter) > 1 or len(guess_letter) < 1):
                print("The letter must be length 1")
                guess_letter = input("Guess the next letter: ").lower() # Guess a letter
            while guess_letter in guess_list or guess_letter in found_list:
                print("You already guessed this letter!")
                guess_letter = input("Guess the next letter: ").lower() # Guess a letter
            for charnum in range(len(word)): #for each letter in the word
        
                if guess_letter == word[charnum]:
                    if found_list[charnum] == "":
                        found_list[charnum] = guess_letter.lower()
                else:
                    if charnum == (len(word) - 1) and guess_letter not in found_list:
                        print("That letter does not exist in the word...")
                        guess_list.append(guess_letter.lower())
                        hang_state += 1
            finalString = ''.join(found_list)
            if str(finalString) == str(word):
                print("You got it! The word was " + word + "!")
                game_end = True

if __name__ == "__main__":
    start()

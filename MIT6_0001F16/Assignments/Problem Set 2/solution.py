# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
   
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
   
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
   
    Starts up an interactive game of Hangman.
   
    '''
     #At the start of the game, let the user know how many
      #letters the secret_word contains and how many guesses s/he starts with.

    print("Welcome to the game Hangman!") 
    length = len(secret_word)   
    print("I'm thinking of a word that is", length, "letters long") 
    ##########################
    #initialise some variables 
    number_guesses = 2
    number_warnings=3
    letters_guessed =''
    word_guess = get_guessed_word(secret_word, letters_guessed)   
    available_letters = get_available_letters(letters_guessed)
    while number_guesses>0:
      #print some messages before ask for guess
      print_messages(number_guesses,letters_guessed)  
      ##get a valid guess
      a=valid_guess(letters_guessed, word_guess, number_guesses, number_warnings)    
      u=updates(number_guesses=a[0],guess=a[1],letters_guessed=letters_guessed, secret_word=secret_word)   
      number_guesses=u[0]
      letters_guessed=u[1]
       ################################
       #check if player has won the game
       #end = is_word_guessed(secret_word, letters_guessed)
       #if end == True:
       #user won calculate winning score 
           #unique = list(set(secret_word))
           #unique_l = (len(unique))
           #score = number_guesses*unique_l
           #print("Congratulations, you won!. The word was", secret_word)
           #print("Your score was", score)          
           #break
      #return(a)        
    #if run out of guesses tell user they lost and reveal word.       
    #print("Sorry you lost, the word was", secret_word)                     

#######################################################
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = load_words()

#select the word
#secret_word = "marina"
#choose_word(wordlist)
#secret_word = "car"
#play hangman
#hangman(secret_word)

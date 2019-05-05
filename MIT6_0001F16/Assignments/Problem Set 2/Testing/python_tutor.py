def print_messages(number_guesses,letters_guessed):
    '''
    number of warnings, number of guesses and letters guessed so far.
    returns: prints how many guesses and the letters available to select from.
    '''
    print("-----------------")        
    print("You have",number_guesses,"guesses remaining")
    #show the available letters to user      
    available_letters = get_available_letters(letters_guessed)
    print("Available letters", available_letters)



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

secret_word="tom"

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    my_String = ''
    for x in secret_word:
         if x in letters_guessed:
              my_String += x
         else:
              my_String += '_ '
    return my_String



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    my_String = ''
    for x in lowercase:
       if x not in letters_guessed:
          my_String += x
    return my_String
    
def valid_guess(letters_guessed, word_guess, 
    number_guesses, number_warnings):
    '''
    user has input an invalid guess, gu\
    inputs: letters guessed, word guess, guess, number of warnings, number or guesses
    returns a guess, number of warnings and number of guesses.
    '''
    #input letter already guessed and lose warning
    
    guess = input("Please guess a letter: ")
    c=guess.isalpha() 
    while c ==False or guess in letters_guessed: 
    #------------------------------  
    #update number of warnings or number of guesses      
      if guess in letters_guessed and number_warnings>0:
        number_warnings=number_warnings-1          
        print("You have already guessed that letter before. You have",
        number_warnings, "warnings left:",word_guess)
        #lose a warning          
      #input letter already guessed and no warnings left so lose a guess
      elif guess in letters_guessed and number_warnings==0:
        number_guesses = number_guesses - 1
        print("You have already guessed that letter before. You have didnt have any warnings left so you lose a guess:", word_guess)
      #guess not in the alphabet and have a warning left  
      elif c == False and number_warnings>0:
         number_warnings=number_warnings-1          
         print("Oops you lost a warning guess not in the alphabet. You have",
         number_warnings, "warnings left.", word_guess)
      elif c == False and number_warnings==0:
        number_guesses = number_guesses - 1
        print("Oops you lost a warning guess not in the alphabet. You have didnt have any warnings left so you lose a guess:", word_guess)
      #Ask for another guess
      print_messages.print_messages(number_guesses,letters_guessed)            
      guess = input("Please guess a letter: ") 
      c=guess.isalpha()   
    return(number_guesses, guess, number_warnings)   

def updates(number_guesses,guess,letters_guessed, secret_word):
  '''purpose: update number of guesses, check if letter is in secret word, give a message to the user if the letter in the word
     and update and print the get guessed word and also available letters
     input: is the output from valid_guess
     returns: number of guesses, available letters and word guess
  '''   
    #######################
    #updates        
    letters_guessed = letters_guessed + guess   
    word_guess = get_guessed_word(secret_word, letters_guessed)   
    #Display to user whether guess in secret word       
    if guess in secret_word:
        print("Good guess", word_guess)
    elif guess in ("a","e","i","o","u"):
        print("Bad guess", word_guess)
        number_guesses = number_guesses -2
    else:   
        print("Bad guess", word_guess)
        number_guesses = number_guesses -1
    return(number_guesses, letters_guessed)
    
hangman(secret_word)  

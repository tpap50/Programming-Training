def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    my_String = True   
    for i in secret_word:
        if i not in letters_guessed:
            my_String = False
    return(my_String)


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

#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print (get_available_letters(letters_guessed))


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


def valid_guess(letters_guessed, word_guess, number_guesses, number_warnings):
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
      print_messages(number_guesses,letters_guessed)            
      #if no more guesses set the guess to null and break, otherwise ask for another guess
      if number_guesses==0:
          guess=''
          break 
      guess = input("Please guess a letter: ") 
      c=guess.isalpha()   
    return(number_guesses, guess, number_warnings) 


def updates(number_guesses,guess,letters_guessed, secret_word):
    '''purpose: update number of guesses, check if letter is in secret word, give a message to the user if the letter in the word
       and update and print the get guessed word and also available letters
       input: is the output from valid_guess
       returns: number of guesses, available letters and word guess
    '''      
    guess_l = list(guess)
    #letters_guessed=list(letters_guessed)
    letters_guessed = letters_guessed + guess_l   
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
    #letters_guessed=''.join(letters_guessed)    
    return(number_guesses, letters_guessed, word_guess)





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
    letters_guessed =['']
    word_guess = get_guessed_word(secret_word, letters_guessed)   
    available_letters = get_available_letters(letters_guessed)
    while number_guesses>0:
      #print some messages before ask for guess
      print_messages(number_guesses,letters_guessed)  
      ##get a valid guess
      a=valid_guess(letters_guessed, word_guess, number_guesses, number_warnings)    
      u=updates(number_guesses=a[0],guess=a[1],letters_guessed=letters_guessed, secret_word=secret_word)   
      number_guesses=u[0]
      number_warnings=a[2]
      letters_guessed=u[1]
      word_guess=u[2]
      #check if user won
      end = is_word_guessed(secret_word, letters_guessed)
      if end == True:
           unique = list(set(secret_word))
           unique_l = (len(unique))
           score = number_guesses*unique_l
           print("Congratulations, you won!. The word was", secret_word)
           print("Your score was", score)          
           break    
    #if run out of guesses tell user they lost and reveal word.       
    print("Sorry you lost, the word was", secret_word)                     
    return(letters_guessed, score, end)
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




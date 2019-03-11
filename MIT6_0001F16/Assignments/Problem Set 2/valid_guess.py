
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
    if guess in letters_guessed and number_warnings>0:
      number_warnings=number_warnings-1          
      print("You have already guessed that letter before. You have",
      number_warnings, "warnings left:",word_guess)
      #lose a warning          
    #input letter already guessed and no warnings left so lose a guess
    elif guess in letters_guessed and number_warnings=0:
      number_guesses = number_guesses - 1
      print("You have already guessed that letter before. You have didnt have any warnings left so you lose a guess")
    #guess not in the alphabet and have a warning left  
    elif c is == False and number_warnings>0:
       number_warnings=number_warnings-1          
       print("Oops you lost a warning guess not in the alphabet. You have",
       number_warnings, "waring left.", word_guess)
    elif c is == False and number_warnings=0:
      number_guesses = number_guesses - 1
      print("Oops you lost a warning guess not in the alphabet. You have didnt have any warnings left so you lose a guess")
    print("-----------------")          
    #print("You have",number_warnings,"warnings remaining")
    print("You have",number_guesses,"guesses remaining")
    #show the available letters to user      
    available_letters = get_available_letters(letters_guessed)
    print("Available letters", available_letters)          
    guess = input("Please guess a letter: ")    
    return(number_guesses, guess, number_warnings)
 
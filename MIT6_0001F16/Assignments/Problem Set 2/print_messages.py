def print_messages(number_warnings,number_guesses,letters_guessed):
    '''
    number of warnings, number of guesses and letters guessed so far.
    returns: prints how many warings, how many guesses and the letters available to select from.
    '''
    print("You have",number_warnings,"warnings remaining") 
    #after each guess need update warnings, guesses, letters guessed and word guess
    print("-----------------")        
    print("You have",number_guesses,"guesses remaining")
    #show the available letters to user      
    #available_letters = get_available_letters(letters_guessed)
    #print("Available letters", available_letters)
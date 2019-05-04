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

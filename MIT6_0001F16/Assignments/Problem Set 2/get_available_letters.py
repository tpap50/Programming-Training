
 
 
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

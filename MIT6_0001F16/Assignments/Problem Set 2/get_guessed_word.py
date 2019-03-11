
 
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
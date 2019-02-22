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

#########
#Testing
#########

#scenario 1 the list is empty
secret_word="marina"
letters_guessed=[]
result=is_word_guessed(secret_word, letters_guessed)
if result == False:
  print("scenario1 test success")
else:
  print("scenario1 test fail")  


#scenario 2 list has some elements but not all letters in the word

secret_word="marina"
letters_guessed=["a","b","c"]
result=is_word_guessed(secret_word, letters_guessed)
if result == False:
  print("scenario2 test success")
else:
  print("scenario2 test fail")  

#scenario 3 list has all the letters in the word 
secret_word="marina"
letters_guessed=["a","r","i","m", "n"]
result=is_word_guessed(secret_word, letters_guessed)
if result == True:
  print("scenario3 test success")
else:
  print("scenario3 test fail")  

#scenario 4 list has all the letters in the word but some are capital letters
secret_word="marina"
letters_guessed=["a","r","i","m", "N"]
result=is_word_guessed(secret_word, letters_guessed)
if result == False:
  print("scenario4 test success")
else:
  print("scenario4 test fail")  


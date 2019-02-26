import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 2")
import solution

'''
def get_guessed_word(secret_word, letters_guessed):

    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.

    my_String = ''
    for x in secret_word:
         if x in letters_guessed:
              my_String += x
         else:
              my_String += '_ '
    return my_String

print(get_guessed_word("marina",[]))    
'''

print(solution.get_guessed_word("marina",["m","A"]))
k = solution.get_available_letters(['m','a','r','i','n','1'])
print(k)
print(solution.valid_input('m', "m_ _ _ _ _ ", "5", 3, 0 ))  

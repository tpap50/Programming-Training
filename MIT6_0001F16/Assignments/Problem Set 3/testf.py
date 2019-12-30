
import pdb
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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

word_list = load_words()

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    failure=True
    word=word.lower()
    if word not in word_list:
       failure=False
    for i in word:
       w=hand.get(i,0)
       if w==0:
          failure=False
          break
    return failure
 




hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
word = "EVIL"


print(is_valid_word(word,hand,word_list))

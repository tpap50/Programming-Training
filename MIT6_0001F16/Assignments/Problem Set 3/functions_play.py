SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_word_score(word,n):
   word=str(word)
   word=word.lower()
   score=0
   for i in word:
	 score_n=SCRABBLE_LETTER_VALUES[i]
	 score=score+score_n
   length=len(word)
   comp2=7*length-(3*(n-length))
   comf=max(comp2,1)
   score_f=score*comf
   return(score_f)







# step 1 we need the hand argument to be a string

def update_hand(hand, word):
  handc=hand.copy()
  for i in word:
    s=handc.get(i,0)
   #lookup in i in hand and if exists we substract 1 from value so long as value is greater than zeor
#1. access the ith element from word
#2  lookup in the hand dictionary use the 'get' function
#3 update hand
    if s > 0:
      handc[i]=handc[i]-1 
  return(handc)


hand = {'j':2, 'o':1, 'l':1, 'w':1, 'n':2}

test=update_hand(hand, 'jolly')
  

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 18:14:53 2019

@author: tompapas
"""

# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:
 
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
 
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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
 
 
 
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
   
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
 
# end of helper code
 
# -----------------------------------
 
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
 


 
def valid_input(letters_guessed, word_guess, guess, number_guesses, number_warnings, c):
    '''
    user has input an invalid guess, gu\
    inputs: letters guessed, word guess, guess, number of warnings, number or guesses
    returns a guess, number of warnings and number of guesses.
    '''
    #input letter already guessed and lose warning
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
 
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
   
    Starts up an interactive game of Hangman.
   
    '''
     #At the start of the game, let the user know how many
      #letters the secret_word contains and how many guesses s/he starts with.
     
    print("Welcome to the game Hangman!") 
    length = len(secret_word)   
    print("I'm thinking of a word that is", length, "letters long") 
    ##########################
    #initialise some variables 
    number_guesses = 6
    number_warnings=3
    letters_guessed =''
    word_guess = get_guessed_word(secret_word, letters_guessed)   
    available_letters = get_available_letters(letters_guessed)
   
    while number_guesses>0:
       ################### 
       #Before each guess 
       print("You have",number_warnings,"warnings remaining") 
       #after each guess need update warnings, guesses, letters guessed and word guess
       print("-----------------")        
       print("You have",number_guesses,"guesses remaining")
       #show the available letters to user      
       available_letters = get_available_letters(letters_guessed)
       print("Available letters", available_letters)
       ##ask user to guess
       guess = input("Please guess a letter: ")
       c=guess.isalpha()
       #######################
       #check if guess valid  
       while c ==False or guess in letters_guessed: 
       #if not valid get a valid guess     
           a=valid_input(letters_guessed, word_guess, guess, number_guesses, number_warnings, c)       
           number_guesses=a[0]
           guess=a[1]
           number_warnings=a[2]
           c=guess.isalpha() 
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
       ################################
       #check if player has won the game
       end = is_word_guessed(secret_word, letters_guessed)
       if end == True:
       #user won calculate winning score 
           unique = list(set(secret_word))
           unique_l = (len(unique))
           score = number_guesses*unique_l
           print("Congratulations, you won!. The word was", secret_word)
           print("Your score was", score)          
           break   
    #if run out of guesses tell user they lost and reveal word.       
    print("Sorry you lost, the word was", secret_word)                     

#######################################################
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = load_words()
 
#select the word
#secret_word = "marina"
#choose_word(wordlist)
#secret_word = "car"
#play hangman
#hangman(secret_word) 
 
 
 
 
######################
# File: Hangman.py
# Author:   A.J. Gauld
# Version: 0.1
#  Date:    2nd April 2000
######################
# Implements a Hangman game based on the game
# framework from game.py
######################

import game, whrandom, string

########### GAME ##########
class Hangman(game.Game):
    wordfile = 'E:\\PROJECTS\\BOOK\\Section4\\hangman.words'
    def __init__(self):
        game.Game.__init__(self)
        self.guessType = hmGuess
        self.outcome = 6    # use outcome to count lives
       
    def displayStart(self):
        self.display(6)

    def getTarget(self):
        return hmTarget()
        
    def getResult(self):
        theWord = ''
        guessed = []
        # generate list of letters guessed so far
        if self.guesses:
            for g in self.guesses:
                guessed.append(g.value())
        # Now check target against guessed letters
        for c in self.theTarget.getGoal():
                    if (c in guessed):
                        theWord =  theWord + c
                    else:
                        theWord = theWord + "_"
        return theWord
    
    def display(self, outcome):
        theWord = self.getResult()
        if  outcome == 1: lives = 'life'
        else: lives = 'lives'
        if '_' in theWord and  outcome == 0:
            print "Sorry you lose, the word was ", self.theTarget.getGoal()
        elif '_' not in theWord:
                print  "Well done, you got it!"
                import sys;sys.exit()
        else:
            print  "Word to guess: %s\t You have %d %s left" % (theWord, outcome, lives)
            
########### GUESS ##########
class hmGuess(game.Guess):
    def __init__(self):
        self.theValue = raw_input("Next letter:  ")
        if len(self.theValue) > 1: self.theValue = self.theValue[0]
        if self.theValue not in string.letters:
            self.theValue = raw_input("It must be a letter! ")

########## TARGET ##########
class hmTarget(game.Target):
    def __init__(self):
        self.lives = 6
        wrdFile = open(Hangman.wordfile, "r")
        wordList =  wrdFile.readlines()
        index = int( whrandom.random() * len(wordList) )
        self.goal = wordList[index][:-1] # lose \n from end

    # eval returns the number of lives left    
    def eval(self, aGuess):
        if aGuess.value() not in self.goal:
            self.lives  = self.lives - 1
        return  self.lives
    
######### DO IT ############
if __name__ == "__main__":
    Hangman().play()
    

# framework for all guessing games
# Game looks after coordination and display
class Game:
    def __init__(self):
        self.theTarget = self.getTarget()
        self.GuessType = Guess
        self.outcome = 1
        self.lives = 1
        self.guesses = []


    # main function, checks score and stops when done    
    def play(self):
        self.displayStart()
        while (self.outcome) and (self.lives > 0):
            self.guesses.append(self.GuessType())
            self.outcome = self.theTarget.eval(self.guesses[-1])
            self.display(self.outcome)
        
    # needs to be overrridden to provide right kind of target
    def getTarget(self):
        return Target()

    #play again, init values and redisplay first 'screen'
    def reStart(self):
        self.__init__()
        self.play()

    # show opening screen - may have instructions etc
    def displayStart(self):
        print """
Abstract class: Game.
You need to create an instance of some specific subclass!"""

    # show appropriate display depending on outcome of last guess
    def display(self, outcome):
        if self.lives == 0:
            self.outcome = 0

# get value(s) from user, present an object for evaluation
class Guess:
    def __init__(self):
        self.theValue = raw_input("Type something: ")

    def value(self):
        return self.theValue

# generate the object to be matched. Check if a guess matches
class Target:
    def __init__(self):
        self.goal = self.getTarget()

    def getTarget(self):
        return 0

    def getGoal(self):
        return self.goal

    def eval(self, aGuess):
        return 0

##############################################################
############### Test Game #############
    
# simple guess the word game - precursor of hangman!
class NameGame(Game):
    names = ['alan','fred','barney','heather','wilma','betty']
    def __init__(self):
        Game.__init__(self)
        self.failMsg = "Sorry, try again."
        self.successMsg = "Well done, you got %s after %d %s."
        self.guessString = 'guess'
        self.theTarget = self.getTarget()
        self.GuessType = NameGuess
        
    def displayStart(self):
        print ("\n\n****************************")

    def getTarget(self):
        return NameTarget()

    def display(self,outcome):
        Game.display(self,outcome)
        if len(self.guesses) > 1:
            self.guessString = "guesses"
        if outcome:
            print self.failMsg
        else:
            print self.successMsg % (self.theTarget.getGoal(),
                                len(self.guesses),
                                self.guessString)

class NameGuess(Guess):
    def __init__(self):
        print NameGame.names
        self.theValue = raw_input("Type a name : ")
        
# ask user for a word to guess, count number of guesses till right
class NameTarget(Target):
    def getTarget(self):
        import whrandom
        return NameGame.names[int(whrandom.random()*len(NameGame.names))]
    
    def eval(self, aGuess):
        if self.goal == aGuess.value():
            return 0
        else:
            return 1

#########################################################
# Create a game and run it.
if __name__ == "__main__":
    w = NameGame()
    w.play()
    w.reStart()
    


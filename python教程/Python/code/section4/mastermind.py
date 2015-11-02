import game,whrandom

class MmTarget(game.Target):
    def __init__(self):
        self.options = [1,2,3,4,5,6]
	self.goal = []
	self.getTarget()
	
    def getTarget(self):
        for i in range(4):
            index = int( whrandom.random() * len(self.options) )
	    self.goal.append(self.options[index])

    def eval(self, aGuess):
        bulls, cows = 0,0
	# create a dictionary of 'what' vv 'how many'
	check = {}
	for i in aGuess.value():
	    if check.has_key(i):
	    	check[i] = check[i] + 1
	    else: check[i] = 1
	# same for the goal
	goalchk = {}
	for i in self.goal:
	    if goalchk.has_key(i):
	    	goalchk[i] = goalchk[i] + 1
	    else: goalchk[i] = 1
	
	# Now total cows = match of guess and goal
	for i in check.keys():
	    if i in self.goal:
	       if goalchk[i] > check[i]:
	           cows = cows + check[i]
	       else: cows = cows + goalchk[i]
	       
	# is it a bull?
        for i in range(4):
	    item = aGuess.value()[i]
	    if item == self.goal[i]:
	       bulls = bulls + 1
	# now reduce cows by number of bulls
	cows = cows - bulls
        return (bulls,cows)

class MmGuess(game.Guess):
    def __init__(self):
        self.theValue = [0,0,0,0]
	print '---------------'
	seq = raw_input('Type 4 digits(between 1 and 6): ')
        for i in range(4):
	   self.theValue[i] = int(seq[i])

class MmGame(game.Game):
    def __init__(self):
        game.Game.__init__(self)
	self.lives = 6
        self.GuessType = MmGuess

    def displayStart(self):
        print 'Try to guess the 4 digits chosen from 1-6'

    def display(self, outcome):
        print 'bulls: %d,  cows: %d' % outcome
        if outcome[0] == 4:
	   print 'Well done, You got it!'
	   self.outcome = 0
	else: 
	   self.lives = self.lives - 1
	if self.lives == 0:
	   print 'Sorry you lose, the target was: ', self.theTarget.getGoal()


    def getTarget(self):
        return MmTarget()

if __name__ == '__main__':
    MmGame().play()
	

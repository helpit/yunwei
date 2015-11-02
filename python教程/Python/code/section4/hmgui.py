from Tkinter import *
import hangman,string

keys = [ ['A','B','C','D'],
         ['E','F','G','H'],
         ['I','J','K','L'],
         ['M','N','O','P'],
         ['Q','R','S','T'],
         ['U','V','W','X'],
         ['Y','Z'] ]

# Guess takes a parameter corresponding to the key clicked
class hmGUIGuess( hangman.hmGuess):
	def __init__(self, ch):
	    self.theValue = string.lower(ch)

# control of the game just passes to Tkinter
# most work is in building the GUI and displaying outcome
class hmGUI(Frame, hangman.Hangman):
	def __init__(self, parent=0):
	    self.imgpath = 'E:\\PROJECTS\\Book\\section4\\'
	    self.firstImg=self.imgpath+'hm6.gif'
	    self.letters = {}
	    hangman.Hangman.__init__(self)
	    Frame.__init__(self,parent)
	    self.master.title('Hangman')
	    self.displayStart()

	def display(self, chr):
	    lossmsg = 'You lost! The word was\n\t%s'
	    playmsg = 'Your target is:\n\t %s'
	    successmsg = 'Well done, you guessed it!'
	    
	    # mark letter as used
	    self.letters[chr].config(state=DISABLED)
	    
	    # create a guess
	    self.guesses.append(hmGUIGuess(chr))
	    
	    # decrease lives if wrong
	    self.lives = self.theTarget.eval(self.guesses[-1])
	    txt = self.getResult()
	    if self.lives > 0: 
		if '_' not in txt:
			txt = successmsg
		else: txt = playmsg % txt
	    else:
		txt = lossmsg % self.theTarget.getGoal()
	    self.status.configure(text=txt) 
	    
	    #now update image
	    thefile = self.imgpath + 'hm' + str(self.lives) + '.gif'
	    self.theImg.configure(file=thefile)

	def getTarget(self):
	    return hangman.hmTarget()
	    
	def quit(self):
	    import sys
	    sys.exit()
	    
	def play(self):
		self.mainloop()

	def reset(self):
	    # mark all letters unused
	    for l in string.uppercase:
		self.letters[l].config(state=ACTIVE)

	    # reset the lives, guesses and create a new target
	    self.lives=6
	    self.guesses = []
	    self.theTarget = self.getTarget()
    
	    # now reset the image and status
	    self.theImg.configure(file=self.firstImg)
	    txt = "Your target is:\n\t%s" % self.getResult()
	    self.status.configure(text=txt)

	def displayStart(self):
		# create display frame with picture on left,
		# letters on right, picture goes inside a text widget
		d = Frame(self)
		hm = Text(d, relief=SOLID, width=25, height=15)
		# create image object
		self.theImg = PhotoImage(file=self.firstImg) 
		# insert @ line 1, char 0
		hm.image_create('1.0', image=self.theImg) 
		hm.pack(side=LEFT, padx=20)

		ltr = Frame(d, bd=1, relief=SUNKEN)
		for row in keys:
		    f = Frame(ltr)
		    for ch in row:
		    	action = lambda x=ch, s=self: s.display(x)
			self.letters[ch] = Button(f, text=ch, 
						width=2, 
						command=action)
			self.letters[ch].pack(side=LEFT)
		    f.pack(pady=1)
		ltr.pack(side=LEFT)
		d.pack()
		
		# Create control frame with status display left, 
		# Reset button middle and Quit button right
		c = Frame(self, border=1, relief=RAISED, background='blue')		
		txt = "Your target is:\n\t%s" % self.getResult()
		self.status = Label(c, anchor=W, 
				bg='blue', fg='yellow', 
				width=25,
				text=txt)
		self.status.pack(side=LEFT,  anchor=W)
		
		r = Button(c, text='Reset', padx=10, command=self.reset)
		r.pack(side=LEFT, padx=10, pady=5, anchor=W)
		
		q = Button(c, text='Quit', padx=10, command=self.quit)
		q.pack(side=RIGHT, padx=20, pady=5, anchor=W)

		c.pack()
		self.pack()

if __name__ == '__main__':
	theGame = hmGUI().play()

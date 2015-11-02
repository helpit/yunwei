from Tkinter import *
import mastermind,game

class MmGuiGuess(game.Guess):
   def __init__(self,text):
       self.theValue = [0,0,0,0]
       for i in range(4): # only take the first 4
           self.theValue[i] = int(text[i])
       

class MmGui(Frame, mastermind.MmGame):
   def __init__(self,parent=0):
      mastermind.MmGame.__init__(self)
      Frame.__init__(self,parent)
      self.master.title("Mastermind")
      self.GuessType = MmGuiGuess
      self.displayStart()

   def quit(self):
      import sys; sys.exit()

   def doit(self):
      if self.lives > 0:
         g = MmGuiGuess(self.guesses[self.lives-1].get()) 
         self.outcome = self.theTarget.eval(g)
         self.display(self.outcome)

   def play(self):
      pass #self.mainloop()

   def display(self,outcome):
      self.lives = self.lives - 1
      self.responses[self.lives].insert(INSERT, "%d, %d" % outcome)
      if outcome[0] == 4:
         self.result['text']="Well done, You got it!"
	 self.lives = 0
      else: 
         if self.lives <= 0:
	    nums = tuple(self.theTarget.getGoal())
	    st = "Sorry you lose, target was %d%d%d%d" % (nums)
            self.result['text']= st

   def displayStart(self):
      'Build GUI'
      # A Label to eventually hold the result
      self.result = Label(self, text="Guess the 4 digit number")
      self.result.pack()
      
      # a Frame for the text boxes
      tf = Frame(self)
      # A frame to hold the guesses
      gf = Frame(tf)
      for i in range(self.lives):
          g = Entry(gf, width='5', relief='sunken')
	  self.guesses.append(g)
	  g.pack()
      # A Frame to hold the responses
      rf = Frame(tf)
      self.responses = []
      for i in range(self.lives):
          r = Entry(rf, width='3', relief='sunken')
	  self.responses.append(r)
	  r.pack()
      tf.pack(side=TOP, padx=40)
      rf.pack(side=RIGHT)
      gf.pack(side=LEFT)
      
      # Buttons to trigger the evaluation and quit
      cnt = Frame(self, relief='raised')
      b = Button(cnt,text="Go figure", command=self.doit)
      q = Button(cnt,text="Quit", command=self.quit)
      b.pack(side=LEFT, padx=5)
      q.pack(side=RIGHT, padx=5)
      cnt.pack(pady=5)
      self.pack()
      self.guesses[self.lives-1].insert(INSERT, "1234")

if __name__ == "__main__":
    MmGui().mainloop()

	

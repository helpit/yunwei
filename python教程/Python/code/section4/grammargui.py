#! /usr/local/bin/python
###########################################################
# File:   	gui.py
# Author: 	A.J. Gauld
# Date:  	24th Dec 1999
#
# Function:
#	A wrapper arounfd  the document classes from grammar 
#       checking created earlier as part of my programming 
#       tutorial. Simply displays a form taking a filename 
#       and allowing selection of text or HTML analysis. 
#       Displays stats in a text widget.
###########################################################

from Tkinter import *
import document

################### CLASS DEFINITIONS ######################
class GrammarApp(Frame):
    def __init__(self, parent=0):
        Frame.__init__(self,parent)
	self.type = 2 # create variable with default value
	self.master.title('Grammar counter')
        self.buildUI()

    def buildUI(self):	
	# the file information: File name and type
	fFile = Frame(self)
	Label(fFile, text="Filename: ").pack(side="left")
	self.eName = Entry(fFile)
	self.eName.insert(INSERT,"test.html")
	self.eName.pack(side="left", padx=5)

	# to keep the radio buttons lined up with the 
	# name we need another frame
	fType = Frame(fFile, borderwidth=1, relief=SUNKEN)
	self.rText = Radiobutton(fType, text="TEXT",
				 variable = self.type, value=2,
				 command=self.doText)
	self.rText.pack(side=TOP)
	self.rHTML = Radiobutton(fType, text="HTML",
	                         variable=self.type, value=1,
				 command=self.doHTML)
	self.rHTML.pack(side=TOP)
	self.rText.select()  # make TEXT the default selection
	fType.pack(side="right", padx=3)
	fFile.pack(side="top", fill=X)
	
	# the text box holds the output, pad it to give a border
        self.txtBox = Text(self, width=60, height=10)
	self.txtBox.pack(side=TOP, padx=3, pady=3)
        
	# finally put some command buttons on to do the real work
	fButts = Frame(self)
	self.bAnal = Button(fButts, 
	                    text="Analyze", 
			    command=self.AnalyzeEvent)
	self.bAnal.pack(side=LEFT, anchor=W, padx=50, pady=2)
	self.bReset = Button(fButts,
	                     text="Reset",
			     command=self.doReset)
	self.bReset.pack(side=LEFT, padx=10)
	self.bQuit = Button(fButts, 
	                    text="Quit", 
			    command=self.doQuitEvent)
	self.bQuit.pack(side=RIGHT, anchor=E, padx=50, pady=2)

	fButts.pack(side=BOTTOM, fill=X)
        self.pack()  

    ################# EVENT HANDLING METHODS ####################
    # time to die...
    def doQuitEvent(self):
        import sys
        sys.exit()
    
    # restore default settings
    def doReset(self):
        self.txtBox.delete('1.0', END)
	self.rText.select()
	
    # set radio values
    def doText(self):
        self.type = 2

    def doHTML(self):
        self.type = 1
	
    # Create appropriate document type and analyze it.
    # then display the results in the form
    def AnalyzeEvent(self):
        filename = self.eName.get()
	if filename == "":
		self.txtBox.insert(END,"\nNo filename provided!\n")
		return
        if self.type == 2:
		doc = document.TextDocument(filename)
	else:
		doc = document.HTMLDocument(filename)
	self.txtBox.insert(END, "\nAnalyzing...\n")
        doc.Analyze()
	str = doc.format % (filename, 
	                    doc.c_paragraph, doc.c_line,
			    doc.c_sentence, doc.c_clause, doc.c_words)
	self.txtBox.insert(END, str)


#################  END OF CLASS DEFINITIONS ################
myApp = GrammarApp()
myApp.mainloop()
 

#! /usr/local/bin/python
################################
# Module: document.py
# Author: A.J. Gauld
# Date:   1999/08/26
# Version: 1.0
################################
# This module provides a Document class which 
# can be subclassed for different categories of 
# Document(text, HTML, Latex etc). Text and 
# a very primitive HTML example are provided.
#
# Primary services available include 
#    - getLines(),
#    - getCharGroups(),
#    - getWords(), 
#    - generateStats(),
#    - printStats().
# Secondary services(for overriding) include:
#    - removeExceptions(),
#    - ltrim(),
#    - rtrim().
################################
import sys,string

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.infile = open(filename,"r")
        self.c_paragraph = 1
        self.c_line, self.c_sentence, self.c_clause, self.c_words = 0,0,0,0
        self.alphas = string.letters + string.digits
        self.stop_tokens = ['.','?','!']
        self.punctuation_chars = ['&','(',')','-',';',':',','] + self.stop_tokens
	self.lines = []
        self.groups = []
        self.c_punctuation = {}
        for c in self.punctuation_chars + self.stop_tokens:
            self.c_punctuation[c] = 0
        self.format = """%s contains:
%d paragraphs, %d lines and %d sentences.
These in turn contain %d clauses and a total of %d words.""" 

    def getLines(self):
        try:
           self.infile = open(self.filename,"r")
           self.lines = self.infile.readlines()
	except:
	   print "Failed to read file ",self.filename
	   sys.exit()

    def getCharGroups(self, lines):
   	for line in lines:
           line = line[:-1]  # lose the '\n' at the end
           self.c_line = self.c_line + 1
           if len(line) == 0: # empty => para break
              self.c_paragraph = self.c_paragraph + 1
           else:
              self.groups = self.groups + string.split(line)
              
    def getWords(self):
        for i in range(len(self.groups)):
	   w = self.groups[i]
           w = self.ltrim(w)
           self.groups[i] = self.rtrim(w)
    
    def removeExceptions(self):
       pass
       
    def ltrim(self,word):
       return word	# do nothing as default
       
    def rtrim(self,word):
       return word	# do nothing as default
        
    def generateStats(self):
        self.c_words = len(self.groups)
        sentences, clauses = 0,0
	for c in self.stop_tokens:
	    sentences = sentences + self.c_punctuation[c] 
	self.c_sentence = sentences 
	for c in self.c_punctuation.keys():
	    clauses = clauses + self.c_punctuation[c]
	self.c_clause = clauses

    def printStats(self):
        print self.format % (self.filename, self.c_paragraph, 
	                     self.c_line, self.c_sentence, 
			     self.c_clause, self.c_words)
        print "The following punctuation characters were used:"
        for i in self.c_punctuation.keys():
            print "\t%s\t:\t%4d" % (i,self.c_punctuation[i])
       
    
    def Analyze(self):
	self.getLines()
        self.getCharGroups(self.lines)
        self.getWords()
        self.removeExceptions()
        self.generateStats()

#########################
# removes blank words after all non 
# alpha chars are stripped        
#########################
class TextDocument(Document):
     def ltrim(self,word):
         while (len(word) > 0) and (word[0] not in self.alphas):
             ch = word[0]
             if ch in self.c_punctuation.keys():
                  self.c_punctuation[ch] = self.c_punctuation[ch] + 1
             word = word[1:]
         return word    
         
     def rtrim(self,word):
         while (len(word) > 0) and (word[-1] not in self.alphas):
             ch = word[-1]
             if ch in self.c_punctuation.keys():
                  self.c_punctuation[ch] = self.c_punctuation[ch] + 1
             word = word[:-1]
         return word    
                
     def removeExceptions(self):
	 top = len(self.groups)
 	 i = 0
	 while i < top:
             if (len(self.groups[i]) == 0):
                del(self.groups[i])
	        top = top - 1
	     i = i+1

#################################
# removes any 'words' begining or 
# ending with '<' or '>' respectively
#################################
class HTMLDocument(TextDocument):
      def removeExceptions(self):
	# use regular expressions to remove all <.+> 
	# clauses from a line. Also any <.i*$ patterns
	# and any ^.*> ones
        import re
	startl = re.compile("^[^<]*>")
	endl = re.compile("<[^>]*$")
	inl = re.compile("<.+>")
	l = 0
	while l < len(self.lines):
	    if len(self.lines[l]) > 1: # if its not blank
		    self.lines[l] = startl.sub('',self.lines[l])
		    self.lines[l] = endl.sub('',self.lines[l])
		    self.lines[l] = inl.sub('',self.lines[l])
		    if len(self.lines[l]) == 1:
		    	del(self.lines[l])
		    else: l = l+1
	    else: l = l+1


      def getWords(self):
	  for i in range(len(self.groups)):
	     w = self.groups[i]
             w = self.ltrim(w)
             self.groups[i] = self.rtrim(w)
	  TextDocument.removeExceptions(self) # now strip empty words

      def Analyze(self):
  	  self.getLines()
          self.removeExceptions()
          self.getCharGroups(self.lines)
          self.getWords()
          self.generateStats()

if __name__ == "__main__":
     if len(sys.argv) <> 2:
        print "Usage: python document.py <filename>"
        sys.exit()
     else:
        try:
           import time
           t = time.time()
           D = HTMLDocument(sys.argv[1])
           D.Analyze()
	   D.printStats()
           print time.time() - t
        except:
	   raise

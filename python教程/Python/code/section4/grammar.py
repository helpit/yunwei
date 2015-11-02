#! /usr/local/bin/python
#############################
# Module: grammar
# Created: A.J. Gauld, 1999,8,19
# 
# Function:
# counts paragraphs, lines, sentences, 'clauses', char groups,
# words and punctuation for a prose like text file. It assumes
# that sentences end with [.!?] and paragraphs have a blank line
# between them. A 'clause' is simply a segment of sentence
# separated by punctuation(braindead but maybe someday we'll 
# do better!)
#
# Usage: Basic usage takes a filename parameter and outputs all
#        stats. Its really intended that a second module use the
#        functions provided to produce more useful commands.
#############################
import string, sys

# initialise global variables
c_paragraph = 1
c_line, c_sentence, c_clause, c_word = 0,0,0,0
groups = []
alphas = string.letters + string.digits
stop_tokens = ['.','?','!']
punctuation_chars = ['&','(',')','-',';',':',','] + stop_tokens
c_punctuation = {}
for c in punctuation_chars:
    c_punctuation[c] = 0
format = """%s contains:
%d paragraphs, %d lines and %d sentences.
These in turn contain %d clauses and a total of %d words.""" 

# use global counter variables and list of char groups
def getCharGroups(infile):
   global c_paragraph, c_line, groups
   try:
      for line in infile.readlines():
          c_line = c_line + 1
          if len(line) == 1: # only a newline so a para break
             c_paragraph = c_paragraph + 1
          else:
             groups = groups + string.split(line)
      return groups
   except:
        print "Failed to read file"
        sys.exit()

def getPunctuation(wordList):
    for item in wordList:
        trim(item)
    # Now delete any empty 'words'
    for i in range(len(wordList)):
        if len(wordList[i]) == 0:
            del(wordList[i])    
            
def trim(item):
    global c_punctuation
    # strip from front
    while (len(item) > 0) and \
          (item[0] not in alphas):
         ch = item[0]
         if ch in c_punctuation.keys():
            c_punctuation[ch] = c_punctuation[ch] + 1
         item = item[1:]
    # now from back
    while (len(item) > 0) and \
          (item[-1] not in alphas):
         ch = item[-1]
         if ch in c_punctuation.keys():
            c_punctuation[ch] = c_punctuation[ch] + 1
         item = item[:-1]    
    
def reportStats():
    global c_sentence, c_clause
    for p in stop_tokens:
        c_sentence = c_sentence + c_punctuation[p]
    for c in c_punctuation.keys():
        c_clause = c_clause + c_punctuation[c]
    print format % (sys.argv[1], 
                    c_paragraph, c_line, c_sentence, 
                    c_clause, len(groups))
    print "The following punctuation characters were used:"
    for p in c_punctuation.keys():
        print "\t%s\t:\t%3d" % (p, c_punctuation[p])
    

def Analyze(infile):
    global groups
    groups = getCharGroups(infile)
    getPunctuation(groups)
    reportStats()
    
if __name__ == "__main__":
     if len(sys.argv) <> 2:
        print "Usage: python grammer.py <filename>"
        sys.exit()
     else:
        import time
        t = time.time()
        Document = open(sys.argv[1],"r")
        Analyze(Document)
	print  time.time() - t

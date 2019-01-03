# Author: Saumya Saxena
# Date: Novemeber 26, 2018
# Assignment 2: Naive Bayes Classifier
# File Name: bayes_template.py - to implement the classifier.

import math, os, pickle, re
from collections import defaultdict
from pathlib import Path
class Bayes_Classifier:

   def __init__(self, trainDirectory = "movies_reviews/"):
      '''This method initializes and trains the Naive Bayes Sentiment Classifier.  If a 
      cache of a trained classifier has been stored, it loads this cache.  Otherwise, 
      the system will proceed through training.  After running this method, the classifier 
      is ready to classify input text.'''

      ''' Step 1  Initialize the positive and negative dictionaries and review directory'''
      self.positiveDict_ = defaultdict(int); self.negativeDict_ = defaultdict(int)
      self.reviewDirectory_ = trainDirectory 

      ''' Step 2  Check if the Classifier Dictionary Cache files exists
                  If cache Files - positive.pickle and negative.pickle
                  do not exists then load them
      '''

      self.positiveFile_ = 'positive.pickle' ; self.negativeFile_ = 'negative.pickle' ; self.totalFile_ = 'total.pickle'
      if ( Path(self.positiveFile_).is_file() and Path(self.negativeFile_).is_file() and Path(self.totalFile_).is_file()):
         self.positiveDict_ = self.load(self.positiveFile_); self.negativeDict_ = self.load(self.negativeFile_)
         self.positiveDocNumber_ = self.load(self.totalFile_)[0]
         self.negativeDocNumber_ = self.load(self.totalFile_)[1]
      else:      
         self.train()

   def train(self):   
      '''Trains the Naive Bayes Sentiment Classifier.'''
      self.positiveDocNumber_ = 0; self.negativeDocNumber_ = 0
      for (root,dirs,files) in os.walk(self.reviewDirectory_, topdown=True):
            for afile in files:
#               print(afile)
               if "txt" in afile:     
                  ftokens = self.tokenize(self.loadFile(self.reviewDirectory_ + afile))
                  reviewRank = 1 if int(afile.split('-')[1]) > 1 else 0
                  if (reviewRank > 0):
                     self.positiveDocNumber_ +=1
                     for token in ftokens :
                        self.positiveDict_[token] += 1
                  else:
                     self.negativeDocNumber_ +=1
                     for token in ftokens :
                        self.negativeDict_[token] += 1
      self.save( self.positiveDict_, self.positiveFile_) 
      self.save( self.negativeDict_, self.negativeFile_)
      l = []
      l.append(self.positiveDocNumber_)
      l.append(self.negativeDocNumber_)
      self.save( l, self.totalFile_) 
    
   def classify(self, sText):
      '''Given a target string sText, this function returns the most likely document
      class to which the target string belongs. This function should return one of three
      strings: "positive", "negative" or "neutral".

      '''
      inputTokens = self.tokenize(sText)
      priorPositive = float(self.positiveDocNumber_)  / float( self.positiveDocNumber_ + self.negativeDocNumber_)
      priorNegative = float(self.negativeDocNumber_)  / float( self.positiveDocNumber_ + self.negativeDocNumber_)



      positiveToken = 0; negativeToken = 0; positiveTotal = 0; negativeTotal = 0;
      for token in inputTokens:
         # print ( token )
         if token in self.positiveDict_.keys() :
            if token in self.negativeDict_.keys():
               positiveToken += math.log(float(self.positiveDict_[token])/float( self.positiveDict_[token] +  self.negativeDict_[token]))
            else:
               positiveToken += math.log(float(1)/float(len(self.positiveDict_)))
         if token in self.negativeDict_.keys():
            if token in self.positiveDict_.keys():
               negativeToken += math.log(float(self.negativeDict_[token])/float( self.positiveDict_[token] +  self.negativeDict_[token]))
            else:
               negativeToken += math.log(float(1)/float(len(self.negativeDict_)))
         # print(positiveToken)
         # print(negativeToken)
      positiveTotal = math.log(priorPositive) + positiveToken
      negativeTotal = math.log(priorNegative) + negativeToken   
      if (( positiveTotal - negativeTotal) > 1.5 ):
         return 'positive' 
      if (( negativeTotal - positiveTotal ) > 1.5):
         return 'negative'
      return 'neutral'


   def loadFile(self, sFilename):
      '''Given a file name, return the contents of the file as a string.'''

      f = open(sFilename, "rb")
      sTxt = f.read()
      f.close()
      return sTxt
   
   def save(self, dObj, sFilename):
      '''Given an object and a file name, write the object to the file using pickle.'''
      print(sFilename)
      f = open(sFilename, "w")
      p = pickle.Pickler(f)
      p.dump(dObj)
      f.close()
   
   def load(self, sFilename):
      '''Given a file name, load and return the object stored in the file.'''

      f = open(sFilename, "r")
      u = pickle.Unpickler(f)
      dObj = u.load()
      f.close()
      return dObj

   def tokenize(self, sText): 
      '''Given a string of text sText, returns a list of the individual tokens that 
      occur in that string (in order).'''

      lTokens = []
      sToken = ""
      for c in sText:
         if re.match("[a-zA-Z0-9]", str(c)) != None or c == "\'" or c == "_" or c == '-':
            sToken += c
         else:
            if sToken != "":
               lTokens.append(sToken)
               sToken = ""
            if c.strip() != "":
               lTokens.append(str(c.strip()))
               
      if sToken != "":
         lTokens.append(sToken)

      return lTokens

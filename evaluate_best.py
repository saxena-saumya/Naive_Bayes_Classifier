# Author: Saumya Saxena
# Date: Novemeber 26, 2018
# Assignment 2: Naive Bayes Classifier
# File Name: evaluate_best.py - to evaluate the performance of improved classifier.

import os

testFile = "bayes.py"
trainDir = "training/"
testDir = "testing/"

execfile(testFile)
bc = Best_Bayes_Classifier(trainDir)
	
iFileList = []

for fFileObj in os.walk(testDir + "/"):
	iFileList = fFileObj[2]
	break
print '%d test reviews.' % len(iFileList)

results = {"negative":0, "neutral":0, "positive":0}

print "\nFile Classifications:"
for filename in iFileList:
	fileText = bc.loadFile(testDir + filename)
	result = bc.classify(fileText)
	print "%s: %s" % (filename, result)
	results[result] += 1

print "\nResults Summary:"
for r in results:
	print "%s: %d" % (r, results[r])
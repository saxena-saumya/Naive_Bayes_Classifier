Author: Saumya Saxena
Date: November 26, 2018
Assignment 2: Naive Bayes Classifier

bayes_template.py implements the Naive Bayes Classifier.

bayes_template_best.py implements the improved Naive Bayes Classifier based on Bi-grams.

bayes.py simply imports the bayes_template.py and bayes_template_best.py

evaluate.py trains and tests the Naive Bayes classifier using bayes_template.py

evaluate_best.py trains and tests the improved Naive Bayes classifier using bayes_template_best.py

Evaluate.txt explains how the improved classifier is better than the regular Naive Bayes Classifier.

To test the program, simply create 3 directories in the same directory which has the above mentioned python files. The three other directories should be:

1) movies_reviews/ - which should have all texts files for the movie reviews.
2) testing/ - which should have files for testing the classifier.
3) training/ - which should have files for training the classifier.

To test the classifier, simply run the command python evaluate.py
To test the improved classifier, simply run the command python evaluate_best.py 
#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
#clf = SVC(kernel="linear")

clf = SVC(kernel='rbf', C=10000)

# select a smaller training set
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print "Accuracy is: ", accuracy

# predict for element 10 of the test set? The 26th? The 50th?
print "10th element: ", pred[10], \
      "\n26th element: ", pred[26], \
      "\n50th element: ", pred[50]

# There are over 1700 test events: how many are predicted to be in the "Chris" (1) class
print """Number predicted to be in the "Chris" class is:""", sum(pred == 1)

#########################################################



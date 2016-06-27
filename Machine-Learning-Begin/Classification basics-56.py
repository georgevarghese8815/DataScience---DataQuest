## 1. Introduction to Classification ##

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# We will use pandas to work with the data
import pandas

# Read file
credit = pandas.read_csv("credit.csv")

# Dataframe of our data
# credit["model_score"] is the probability provided by the model
# credit["paid"] is the observed payments
# .head(10) shows the first 10 rows of the dataframe
plt.scatter(credit["model_score"], credit["paid"])
plt.show()

## 2. Predictive Power ##

# Will we approve the credit card based on the probability of paying?
pred = credit["model_score"] > 0.5

# This operation tells us whether the prediction was correct 
a = (pred == credit["paid"])
accuracy = a[a == True].shape[0]/credit.shape[0]

#Alternate
accuracy = sum(pred == credit["paid"]) / len(pred)

## 3. Measures of Binary Discrimination ##

# prediction with discrimination threshold at 0.50
pred = credit["model_score"] > 0.5
print(type(pred))
# number of true positives
TP = sum(((pred == 1) & (credit["paid"] == 1)))
print(TP)
FN = sum(((pred == 0) & (credit["paid"] == 1)))

## 4. Sensitivity, Specificity, and Fall-Out ##

# Predicted to play tennis
pred = credit["model_score"] > 0.5

# Number of true negatives
TN = sum(((pred == 0) & (credit["paid"] == 0)))

# Number of false positives
FP = sum(((pred == 1) & (credit["paid"] == 0)))

# Number of True positives
TP = sum(((pred == 1) & (credit["paid"] == 1)))

# Number of False Negatives
FN = sum(((pred == 0) & (credit["paid"] == 1)))

# Compute the false positive rate
FPR = FP / (TN + FP)
print(FPR)

# this is right
TPR = TP / (TP + FN)

# Ignore this answer
TPR = TP / (TP + FP)

## 6. Computing ROC Curves ##

import numpy

def roc_curve(observed, probs):
    # choose thresholds between 0 and 1 to discriminate prediction
    thresholds = numpy.asarray([(100-j)/100 for j in range(100)])
    
    # initialize false and true positive rates 
    fprs = numpy.asarray([0. for j in range(100)])
    tprs = numpy.asarray([0. for j in range(100)])
    
    # Loop through each threshold
    for j, thres in enumerate(thresholds):
        # Using the new threshold compute predictions
        pred = probs > thres
        # Count the Number of False Positives
        FP = sum((observed == 0) & (pred == 1))
        # Count the Number of True Negatives 
        TN = sum((observed == 0) & (pred == 0))
        # Compute the False Postive Rate
        FPR =  float(FP / (FP + TN))
        # Count the number of True Positives
        TP = sum((observed == 1) & (pred == 1))
        # Count the number of False Negatives
        FN = sum((observed == 1) & (pred == 0))
        # Compute the True Positive Rate
        TPR = float(TP / (TP + FN))
        # Store the true and false positive rates
        fprs[j] = FPR
        tprs[j] = TPR
        
    return fprs, tprs, thresholds

fpr, tpr, thres = roc_curve(credit["paid"], credit["model_score"])
idx = numpy.where(fpr>0.20)[0][0]
print(tpr[idx])
print(thres[idx])
plt.plot(fpr, tpr)
plt.show()

## 8. Area Under the Curve ##

from sklearn.metrics import roc_auc_score

probs = [ 0.98200848,  0.92088976,  0.13125231,  0.0130085,   0.35719083,  
         0.34381803, 0.46938187,  0.53918899,  0.63485958,  0.56959959]
obs = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1]

testing_auc = roc_auc_score(obs, probs)
print("Example AUC: {auc}".format(auc=testing_auc))
auc = roc_auc_score(credit["paid"], credit["model_score"])

## 9. Precision and Recall ##

pred = credit["model_score"] > 0.5

# True Positives
TP = sum(((pred == 1) & (credit["paid"] == 1)))
print(TP)

# False Positives
FP = sum(((pred == 1) & (credit["paid"] == 0)))
print(FP)

# False Negatives
FN = sum(((pred == 0) & (credit["paid"] == 1)))
print(FN)
precision = TP/(TP+FP)
recall = TP/(TP+FN)

## 10. Precision and Recall Curve ##

from sklearn.metrics import precision_recall_curve

probs = [ 0.98200848,  0.92088976,  0.13125231,  0.0130085,   0.35719083,  
         0.34381803, 0.46938187,  0.53918899,  0.63485958,  0.56959959]
obs = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1]

precision, recall, thresholds = precision_recall_curve(obs, probs)
precision, recall, thresholds = precision_recall_curve(credit["paid"], credit["model_score"])
plt.plot(recall, precision)
plt.show()
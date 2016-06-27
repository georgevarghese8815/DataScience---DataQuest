## 1. Introduction to the Data ##

import pandas
import matplotlib.pyplot as plt

# load income data from a previous lesson
us_income = pandas.read_csv("us_income.csv")

# Scatter plot 
plt.scatter(us_income["median_income"], us_income["median_income_graduate_degree"])
plt.show()
admissions = pandas.read_csv("admissions.csv")
plt.scatter(admissions["gpa"], admissions["admit"])
plt.show()

## 2. Use Linear Regression to Predict Admission ##

# The admissions DataFrame is in memory

# Import linear regression class
from sklearn.linear_model import LinearRegression

# Initialize a linear regression model
model = LinearRegression()

# Fit model
model.fit(admissions[['gre', 'gpa']], admissions["admit"])

# This is how we can predict a new observation given gre=600 and gpa=3.0
print(model.predict([[600., 3.0]]))

model = LinearRegression()
model.fit(admissions[['gre', 'gpa']], admissions["admit"])
admit_prediction = model.predict(admissions[['gre', 'gpa']])

#Scatter plot
plt.scatter(admissions["gpa"], admit_prediction)
plt.show()


## 4. The Logit Function ##

# Logistic Function
def logit(x):
    # np.exp(x) raises x to the exponential power, ie e^x. e ~= 2.71828
    return np.exp(x) / (1 + np.exp(x)) 

# Linspace is as numpy function to produce evenly spaced numbers over a specified interval.
# Create an array with 50 values between -6 and 6 as t
t = np.linspace(-6,6,50, dtype=float)

# Get logistic fits
ylogit = logit(t)

# plot the logistic function
plt.plot(t, ylogit, label="logistic")
plt.ylabel("Probability")
plt.xlabel("t")
plt.title("Logistic Function")
plt.show()
a = logit(-10)
b = logit(10)

## 5. Bernoulli Random Variable ##

# Enter your code here.
biased_heads = 60*0.6

## 7. Model Data ##

from sklearn.linear_model import LogisticRegression

# Randomly shuffle our data for the training and test set
admissions = admissions.loc[np.random.permutation(admissions.index)]

# train with 700 and test with the following 300, split dataset 
num_train = 700
data_train = admissions[:num_train]
data_test = admissions[num_train:]

# Fit Logistic regression to admit with gpa and gre as features using the training set
logistic_model = LogisticRegression()
logistic_model.fit(data_train[["gpa", "gre"]], data_train['admit'])

# Print the Models Coefficients
print(logistic_model.coef_)

# Predict the chance of admission from those in the training set
fitted_vals = logistic_model.predict_proba(data_train[['gpa', 'gre']])[:,1]

#Applying the model on the test set
fitted_test = logistic_model.predict_proba(data_test[["gpa", "gre"]])[:,1]

plt.scatter(data_test["gre"], fitted_test)
plt.show()






## 8. Predictive Power ##

# .predict() using a threshold of 0.50 by default
predicted = logistic_model.predict(data_train[['gpa','gre']])

# The average of the binary array will give us the accuracy
accuracy_train = (predicted == data_train['admit']).mean()

# Print the accuracy
print("Accuracy in Training Set = {s}".format(s=accuracy_train))

#Calculations on Test set
percent_admitted = data_test["admit"].mean() * 100

# Predicted to be admitted
predicted = logistic_model.predict(data_test[['gpa','gre']])

# What proportion of our predictions were true
accuracy_test = (predicted == data_test['admit']).mean()

## 9. Admissions ROC Curve ##

from sklearn.metrics import roc_curve, roc_auc_score

# Compute the probabilities predicted by the training and test set
# predict_proba returns probabilies for each class.  We want the second column
train_probs = logistic_model.predict_proba(data_train[['gpa', 'gre']])[:,1]
test_probs = logistic_model.predict_proba(data_test[['gpa', 'gre']])[:,1]

auc_train = roc_auc_score(data_train["admit"], train_probs)
auc_test = roc_auc_score(data_test["admit"], test_probs)
# Difference in auc values
auc_diff = auc_train - auc_test

# Compute ROC Curves 
roc_train = roc_curve(data_train["admit"], train_probs)
roc_test = roc_curve(data_test["admit"], test_probs)

# Plot false positives by true positives
plt.plot(roc_train[0], roc_train[1])
plt.show()
plt.plot(roc_test[0], roc_test[1])
plt.show()
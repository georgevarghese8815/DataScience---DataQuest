## 3. Remove columns ##

# The 1 specifies that we need to drop a column.
event_frame = event_frame.drop("id", axis=1)

## 4. Convert text fields ##

# Split the data into groups.
groups = event_frame.groupby("session_id")

# Make a dictionary that maps events to codes.
event_codes = {
    'started-mission': 1,
    'started-screen': 2,
    'run-code': 3,
    'next-screen': 4,
    'get-answer': 5,
    'reset-code': 6,
    'interactive-mode-start': 7,
    'show-hint': 8,
    'open-forum': 9
}

all_predictors = []
for name, group in groups:
    # Sort the group
    group = group.sort(["created_at"], ascending=[1])
    
    # Replace the values in the event_type column with their corresponding codes.
    # The .apply method applies a function to each item in a series or dataframe in turn.
    # The lambda function will return the result of looking up the event_type
    # value in the event_codes dictionary.
    event_type = group["event_type"].apply(lambda x: event_codes[x])
    # Make a dataframe
    predictor_frame = pd.DataFrame({
                "event_type": event_type
            })
    # Add the predictor frame to the list of predictor frames
    # We'll concatenate everything in this list later to make our predictor frame.
    all_predictors.append(predictor_frame)

## 5. Adding more columns ##

groups = event_frame.groupby("session_id")

all_predictors = []
for name, group in groups:
    group = group.sort(["created_at"], ascending=[1])
    
    # Convert the created_at column to a datetime type, so we can do math with it.
    group['created_at'] = group['created_at'].astype('datetime64[ns]')
    predictor_frame = pd.DataFrame({
                "event_type": group["event_type"].apply(lambda x: event_codes[x]),
                # Find the total seconds between the current event and the first event in the session.
                "session_time": group["created_at"].apply(lambda x: (x - group["created_at"].iloc[0]).total_seconds())
            })

    all_predictors.append(predictor_frame)

## 6. Number of previous events column ##

groups = event_frame.groupby("session_id")

all_predictors = []
for name, group in groups:
    group = group.sort(["created_at"], ascending=[1])
    group['created_at'] = group['created_at'].astype('datetime64[ns]')

    predictor_frame = pd.DataFrame({
                "event_type": group["event_type"].apply(lambda x: event_codes[x]),
                "session_time": group["created_at"].apply(lambda x: (x - group["created_at"].iloc[0]).total_seconds()),
                # Generate a sequence the same length as the number of rows in the group.
                # It will start at 0, and end at the length of the group.
                # Because of the fact that the group is sorted in ascending order,
                # this is also a counter of number of previous events.
                "session_events": range(group.shape[0])
            })

    all_predictors.append(predictor_frame)

## 7. Number of events on current screen ##

groups = event_frame.groupby("session_id")

all_predictors = []
for name, group in groups:
    group = group.sort(["created_at"], ascending=[1])
    group['created_at'] = group['created_at'].astype('datetime64[ns]')
    
    # Compute how many events occured on each screen.
    screen_events = []
    counter = 0
    prev_sequence = None
    for sequence in group["sequence"]:
        if sequence == prev_sequence:
            counter += 1
        else:
            counter = 0
        prev_sequence = sequence
        screen_events.append(counter)

    predictor_frame = pd.DataFrame({
                "event_type": group["event_type"].apply(lambda x: event_codes[x]),
                "session_time": group["created_at"].apply(lambda x: (x - group["created_at"].iloc[0]).total_seconds()),
                "session_events": range(group.shape[0]),
                "screen_events": screen_events
            })

    all_predictors.append(predictor_frame)

## 10. Train and test split ##

import math

# Decide where to split the data -- we want the first 70% in the training set.
train_thresh = math.floor(len(all_predictors) * .7)

# Split the list of dataframes
train = all_predictors[:train_thresh]
test = all_predictors[train_thresh:]

# Concatenate all the items in the split lists.
# Concatenate them along the row axis.
# This results in one big dataframe.
train = pd.concat(train, axis=0)
test = pd.concat(test, axis=0)

# Around 6000 rows in the training data.
print(train.shape[0])

# Around 1000 rows in the test data.
print(test.shape[0])

## 11. Training the algorithm ##

from sklearn.linear_model import LogisticRegression

predictors = ['event_type', 'screen_events', 'session_events', 'session_time']
clf = LogisticRegression()
clf.fit(train[predictors], train["target"])

# Make predictions of the probability that the row is a 0 or a 1.
predictions = clf.predict_proba(test[predictors])

## 12. Measuring error ##

from sklearn.metrics import roc_auc_score

# This is the score of our classifier.  We want to compare our target against 
# the probability that the row is a 1 (the second column of the predictions).
print(roc_auc_score(test["target"], predictions[:,1]))
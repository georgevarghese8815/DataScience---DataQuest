## 2. Matching attempts to progress ##

# Generate a boolean series that is True whenever a row in attempts_frame has its 
# screen_progress column equal to the pk of the 1138th row in progress_frame.
# This will find all the attempts linked to the 1138th row in progress_frame.
has_progress_row_id = attempt_frame["screen_progress"] == progress_frame["pk"][1137]

# Actually select the rows from the attempt_frame
progress_attempts = attempt_frame[has_progress_row_id]

# The .shape attribute of a dataframe contains information about how many rows and columns it has
# .shape returns a list -- the first number is the row count, the second is the column count.
# We're printing the row count below.
print(progress_attempts.shape[0])
correct_attempts_count = progress_attempts[progress_attempts["correct"] == True].shape[0]
incorrect_attempts_count = progress_attempts[progress_attempts["correct"] == False].shape[0]
print(progress_frame["pk"][1137])

## 3. Figuring out attempt ratios ##

import numpy as np
import matplotlib.pyplot as plt

# Split the data into groups
groups = attempt_frame.groupby("screen_progress")

ratios = []
# Compute ratios for each group
# Loop over each group, and compute the ratio.
for name, group in groups:
    # The ratio we want is the number of correct attempts divided by the total number of attempts.
    # Taking the mean of the correct column will do this.
    # If you take the sum or mean of a boolean column, True values will become 1, and False values 0.
    ratio = np.mean(group["correct"])
    
    # Add the ratio to the ratios list.
    ratios.append(ratio)

# This code does the same thing as the segment above, but it's simpler.
# We aggregate across each group using the np.mean function.
# This takes the mean of every column in each group, then makes a dataframe with all the means.
# We only care about correctness, so we only select the correct column at the end.
easier_ratios = groups.aggregate(np.mean)["correct"]

# We can plot a histogram of the easier_ratios series.
# The kind argument specifies that we want a histogram.
# Histograms show how values are distributed -- in this case, 900 of the screens have only 1 (correct) attempt.
# Many more appear to have had two attempts (a .5 ratio).
easier_ratios.plot(kind="hist")
plt.show()

groups2 = attempt_frame.groupby("screen_progress")
ratios = groups2.aggregate(len)["correct"]

ratios.plot(kind = "hist", bins = 15)
plt.show()

## 4. Who gives up? ##

# Enter code here.
gave_up_ids = progress_frame["pk"][progress_frame["complete"] == False]

## 5. Graphing attempt counts ##

gave_up_boolean = attempt_frame["screen_progress"].isin(gave_up_ids)
gave_up_attempts = attempt_frame[gave_up_boolean]
groups = gave_up_attempts.groupby("screen_progress")
attempts = groups.aggregate(len)["correct"]
attempts.plot(kind = "hist")
plt.show()

## 6. Attempt count differential ##

gave_up = attempt_frame[attempt_frame["screen_progress"].isin(gave_up_ids)]
groups = gave_up.groupby("screen_progress")
counts = groups.aggregate(len)["correct"]

# We can use the .mean() method on series to compute the mean of all the values.
# This is how many attempts, on average, people who gave up made.
print(counts.mean())

# We can filter our attempts data to find who didn't give up (people that got the right answer).
# To do this, we use the ~ operator.
# It negates a boolean, and swaps True and False.
# This filters for all rows that aren't in gave_up_ids.
eventually_correct = attempt_frame[~attempt_frame["screen_progress"].isin(gave_up_ids)]
groups2 = eventually_correct.groupby("screen_progress")
counts2 = groups2.aggregate(len)["correct"]

average_attempts_if_correct = counts2.mean()

## 7. Another data store ##

# We have 200 sessions
print(len(sessions))

# The first session has 38 student events
print(len(sessions[0]))

# Here's a single event from the first user session -- it's a started-screen event
print(sessions[0][3])

# We'll make a histogram of event counts per session
plt.hist([len(s) for s in sessions])
plt.show()

## 8. Event structure ##

# Where we'll put the events after we "flatten" them
flat_events = []

# If we're going to combine everything in one dataframe, we need to keep 
# track of a session id for each session, so we can link events across sessions.
session_id = 1

# Loop through each session.
for session in sessions:
    # Loop through each event in each session.
    for event in session:
        new_event = {
            "session_id": session_id,
            # We use .get() to get the fields that could be missing.
            # .get() will return a default null value if the key isn't found in the dictionary.
            # If we used regular indexing like event["mission"], we would get an
            # error if the key wasn't found.
            "mission": event.get("mission"),
            "type": event.get("type"),
            "sequence": event.get("sequence")
        }
        new_event["id"] = event["keen"]["id"]
        new_event["created_at"] = event["keen"]["created_at"]
        new_event["event_type"] = event["event_type"]
        # Insert code here to add the rest of the events to new_event.
        flat_events.append(new_event)
    session_id += 1

## 9. Convert to dataframe ##

# Enter your code here.
event_frame = pd.DataFrame(flat_events)

## 10. Exploring the session data ##

# Sort event_frame in ascending order of created_at.
event_frame = event_frame.sort(["created_at"], ascending = True)

# Group events by session
groups = event_frame.groupby("session_id")
groups = event_frame.groupby("session_id")

ending_events = []
for name, group in groups:
    # The .tail() method will get the last few events from a dataframe.
    # The number you pass in controls how many events it will take from the end.
    # Passing in 1 ensures that it only takes the last one.
    last_event = group["event_type"].tail(1)
    ending_events.append(last_event)
    
# The concat method will combine a list of series into a dataframe.
ending_events = pd.concat(ending_events)
ending_event_counts = ending_events.value_counts()
ending_event_counts.plot(kind = "bar")
plt.show()

## 11. Most common events ##

# Enter your code here.
event_counts = event_frame["event_type"].value_counts()
event_counts.plot(kind="bar")
plt.show()

## 13. Mission numbers ##

# Enter your code here
event_counts = event_frame["mission"].value_counts()
event_counts.plot(kind = "bar")
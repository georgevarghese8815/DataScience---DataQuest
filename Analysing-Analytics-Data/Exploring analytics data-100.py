## 2. A quick look at dataquest ##

# This is the code area, where you can type and execute code.
# You can assign values to variables here, or anything else you want to do.
# Anything that starts with a # is a comment, and is used for explanation, but isn't executed as code.

a = 5
print(5)

## 3. Looking at student data ##

# The attempts are stored in the attempts variable, and progress is stored in the progress variable.

# Here's how one progress record looks.
print("Progress Record:")
# Pretty print is a custom function we made to output json data in a nicer way.
pretty_print(progress[0])
print("\n")

# Here's how one attempt record looks.
print("Attempt Record:")
pretty_print(attempts[0])

## 4. Lists ##

arnold_movies = ["Terminator", "Predator", "Total Recall", "Conan the Barbarian"]

# We can add items to a list using .append.
# If for some reason, we want to acknowledge Kindergarten Cop as a movie, we can do this...
arnold_movies.append("Kindergarten Cop")

# We can get the second item in a list
print(arnold_movies[1])
bad_arnold_movies = ["Junior", "Batman & Robin", "Kindergarten Cop"]

## 5. Dictionaries ##

# Dictionaries are easy to define
boston = {
        "name": "Boston",
        "type": "major city",
        "population": 650000,
        "weather": "ridiculously bad"
    }

# We can add keys to dictionaries
boston["education_level"] = "high!"
print(boston)
    
# We can also nest dictionaries.
cities = {
        "Boston": {
            "weather": "ridiculously bad"
        },
        "San Francisco": {
            "weather" : "okay, better than Boston at least"
        },
        "San Diego": {
            "weather" : "why haven't you moved here yet?"
        }
    }
    

weird_presidential_facts = [{"name": "Benjamin Harrison", "oddity": "Afraid of electricity."}, {"name": "Theodore Roosevelt", "oddity": "Had a pet badger named Josiah who bit people."}, {"name": "Andrew Jackson", "oddity": "Taught his parrot to curse."}]

## 6. The structure of the data ##

# This gets the fields attribute from the first attempt, and prints it
# As you can see, fields is another dictionary
# The keys for fields are listed above
pretty_print(attempts[0]["fields"])
print("\n")

# This gets the "correct" attribute from "fields" in the first attempt record
print(attempts[0]["fields"]["correct"])
print("\n")

fourth_progress_last_code = progress[3]["fields"]["last_code"]
third_attempt_progress = attempts[2]["fields"]["screen_progress"]

## 7. Exploring the data ##

# Number of screens students have seen
progress_count = len(progress)
print(progress_count)

# Number of attempts
attempt_count = len(attempts)
print(attempt_count)

average_attempts = attempt_count / progress_count

## 8. Getting to user level data ##

# A list to put the user ids
all_user_ids = []

# A for loop lets us repeat code.  
# In this case, we're pulling each record from the progress list, in order, 
# and doing a manipulation.
for record in progress:
    user_id = record["fields"]["user"]
    all_user_ids.append(user_id)

# This pulls out only the unique user ids
all_user_ids = list(set(all_user_ids))

print(all_user_ids[0])
count = 0
for record in progress:
    if record["fields"]["user"] == 51331:
        count += 1
id_51331_count = count

## 9. Vectors ##

# We can import python package like this.
import numpy

# The numpy asarray method converts a list to an array.
vector = numpy.asarray([1,2,3,4])
element_1 = vector[0]
element_3 = vector[2]

## 10. Matrices ##

# If we use the as keyword, we can import something, but rename it to a shorter name
# This makes it easier when we do analysis because we don't have to type the full name
import numpy as np

# If we pass a list of lists to asarray, it converts them to a matrix.
matrix = np.asarray([
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
    ])
matrix_1_1 = matrix[1,1]
matrix_0_2 = matrix[0,2]

## 11. Pandas dataframes ##

# "Flatten" the progress records out.
flat_progress = []
for record in progress:
    # Get the fields dictionary, and use it as the start of our flat record.
    flat_record = record["fields"]
    # Store the pk in the dictionary
    flat_record["pk"] = record["pk"]
    
    # Add the flat record to flat_progress
    flat_progress.append(flat_record)

flat_attempts = []
for record_a in attempts:
    flat_record_a = record_a["fields"]
    flat_record_a["pk"] = record_a["pk"]
    
    flat_attempts.append(flat_record_a)

## 12. Creating dataframes ##

import pandas as pd

progress_frame = pd.DataFrame(flat_progress)
# Print the names of the columns
print(progress_frame.columns)

# Print the first 5 rows of the data
print(progress_frame.head(5))

attempt_frame = pd.DataFrame(flat_attempts)

## 13. Indexing dataframes ##

# Get all the unique values from a column.
user_ids = progress_frame["user"].unique()

# Make a table of how many screens each user attempted
user_id_counts = progress_frame["user"].value_counts()
print(user_id_counts)

screen_counts = progress_frame["screen"].value_counts()

## 14. Making charts ##

# Import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt

# Plot how many screens each user id has seen.
# The value_counts method sorts everything in descending order.
user_counts = progress_frame["user"].value_counts()

# The range function creates an integer range from 1 to the specified number.
x_axis = range(len(user_counts))

# Make a bar plot of the range labels against the user counts.
plt.bar(x_axis, user_counts)

# We have to use this to show the plot.
plt.show()

plt.bar(range(len(progress_frame["screen"].value_counts())), progress_frame["screen"].value_counts())
plt.show()

## 15. Pandas filtering ##

user_id_46578 = progress_frame["user"] == 46578
# See how all the values are either True or False?
print(user_id_46578)

screen_1 = progress_frame["screen"] == 1

## 16. On to filtering! ##

# Enter code here
screen_1_frame = progress_frame[progress_frame["screen"] == 1]
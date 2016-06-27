## 2. College majors and employment ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
all_ages.head(5)

## 3. Summarizing major categories ##

# All values for Major_category
# print(all_ages['Major_category'].value_counts().index)
import pandas as pd

all_ages_major_categories = dict()
recent_grads_major_categories = dict()
M_category = all_ages['Major_category'].value_counts().index.tolist()
for item in M_category:
    temp = all_ages[all_ages["Major_category"] == item]
    all_ages_major_categories[item] = temp["Total"].sum()
    temp2 = recent_grads[recent_grads["Major_category"] == item]
    recent_grads_major_categories[item] = temp2["Total"].sum()

## 4. Low wage jobs rates ##

low_wage_percent = recent_grads["Low_wage_jobs"].sum() / recent_grads["Total"].sum()

## 5. Comparing datasets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index

recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0
for item in majors:
    temp1 = recent_grads[recent_grads["Major"] == item]
    temp2 = all_ages[all_ages["Major"] == item]
    Rate1 = temp1["Unemployment_rate"].values[0]
    Rate2 = temp2["Unemployment_rate"].values[0]
    if Rate1 < Rate2:
        recent_grads_lower_emp_count += 1
    elif Rate2 < Rate1:
        all_ages_lower_emp_count += 1
        
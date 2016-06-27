## 3. Exploring the data ##

import pandas as pd
import numpy as np
avengers = pd.read_csv("avengers.csv")
avengers.head(5)
print(avengers.columns.tolist())
print(avengers.dtypes)

## 4. Filter out the bad years ##

import matplotlib.pyplot as plt
%matplotlib inline
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year'] > 1960]
true_avengers['Year'].hist()

## 5. Consolidating deaths ##

columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
true_avengers[columns]
def clean_deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            num_deaths += 1
    return num_deaths
    
true_avengers["Deaths"] = true_avengers[columns].apply(lambda row: clean_deaths(row), axis = 1)

## 6. Years since joining ##


joined_accuracy_count  = 0
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)
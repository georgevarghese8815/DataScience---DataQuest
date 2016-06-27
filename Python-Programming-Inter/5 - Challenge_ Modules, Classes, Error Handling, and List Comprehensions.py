## 1. Introduction to the data ##

import csv
a = open("nfl_suspensions_data.csv", "r")
b = csv.reader(a)
nfl_suspensions = list(b)
nfl_suspensions = nfl_suspensions [1:len(nfl_suspensions)]

years = {}
for item in nfl_suspensions:
    if item[5] in years:
        years[item[5]] += 1
    else:
        years[item[5]] = 1
print(years)

## 2. Unique values ##

a = [item[1] for item in nfl_suspensions]
unique_teams = set(a)
b = [item[2] for item in nfl_suspensions]
unique_games = set(b)
print(unique_teams)
print(unique_games)

## 3. Suspension class ##

class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]

third_suspension = Suspension(nfl_suspensions[2])

## 4. Tweaking the Suspension class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[3])
        except Exception:
            self.year = 0
    
    def get_year(self):
        return(self.year)
        
missing_year = Suspension(nfl_suspensions[23])
zero = missing_year.get_year()
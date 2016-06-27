## 3. Read in a CSV file ##

import pandas as p
food_info = p.read_csv("food_info.csv")
print(type(food_info))

## 4. Exploring the DataFrame ##

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)
first_twenty = food_info.head(20)

## 7. Selecting a row ##

print(food_info.loc[0])
print(food_info.loc[6])
hundredth_row = food_info.loc[99]
print(hundredth_row)

## 8. Data types ##

print(food_info.dtypes)

## 9. Selecting multiple rows ##

print("Rows 3, 4, and 5")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])
num_rows = food_info.shape[0]
last_rows = food_info[num_rows-5:num_rows]

## 10. Selecting individual columns ##

# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

## 11. Selecting multiple columns by name ##

zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
selenium_thiamin = food_info[["Selenium_(mcg)", "Thiamin_(mg)"]]

## 12. Practice ##

print(food_info.columns)
print(food_info.head(2))
cols = food_info.columns.tolist()
gram_columns = []
for item in cols:
    if item.endswith("(g)") == True:
        gram_columns.append(item)
gram_df = food_info[gram_columns]
gram_df.head(3)
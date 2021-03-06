## 1. Overview ##

import pandas as p
food_info = p.read_csv("food_info.csv")
test = food_info.columns
cols = food_info.columns.tolist()
food_info.loc[0:3]

## 2. Transforming a column ##

div_100 = food_info["Iron_(mg)"] / 1000
add_100 = food_info["Iron_(mg)"] + 100
sub_100 = food_info["Iron_(mg)"] - 100
mult_2 = food_info["Iron_(mg)"]*2
sodium_grams = food_info["Sodium_(mg)"]/1000
sugar_milligrams = food_info["Sugar_Tot_(g)"]*1000

## 3. Math with columns ##

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])
grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]

## 4. Nutritional index ##

weighted_protein = 2 * food_info["Protein_(g)"]
weighted_fat = -0.75 * food_info["Lipid_Tot_(g)"]
initial_rating = weighted_protein + weighted_fat

## 5. Normalizing columns ##

print(food_info["Protein_(g)"][0:5])
max_protein = food_info["Protein_(g)"].max()
normalized_protein = food_info["Protein_(g)"] / max_protein
print(normalized_protein[0:5])
max_fat = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / max_fat

## 6. Creating a new column ##

max_protein = food_info["Protein_(g)"].max()
Normalized_Protein = food_info["Protein_(g)"] / max_protein
food_info["Normalized_Protein"] = Normalized_Protein
max_fat = food_info["Lipid_Tot_(g)"].max()
Normalized_Fat = food_info["Lipid_Tot_(g)"] / max_fat
food_info["Normalized_Fat"] = Normalized_Fat


## 7. Normalized nutritional index ##

food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Norm_Nutr_Index"] = (2 * food_info["Normalized_Protein"]) - (0.75 * food_info["Normalized_Fat"] )

## 8. Sorting a DataFrame by a column ##

food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Lipid_Tot_(g)"])
food_info.sort("Norm_Nutr_Index", inplace = True, ascending = False)
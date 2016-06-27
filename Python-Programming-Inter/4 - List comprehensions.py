## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, item in enumerate(ships):
    print(item)
    print(cars[i])

## 3. Adding columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, item in enumerate(things):
    item.append(trees[i])
print(things)

## 4. List comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [2*apple for apple in apple_prices]
apple_prices_lowered  = [apple - 100 for apple in apple_prices]

## 5. Counting up female names ##

name_counts = {}
for item in legislators:
    if item[3] == "F" and item[7] > 1940:
        if item[1] in name_counts:
            name_counts[item[1]] += 1
        else:
            name_counts[item[1]] = 1

print(name_counts)

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for item in values:
    a = item is not None and item > 30
    checks.append(a)
print(checks)

## 8. Highest female name count ##

max_value = None
for item in name_counts:
    count = name_counts[item]
    if max_value is None or count > max_value:
        max_value = count
        max_key = item
print(max_value)
print(max_key)

## 9. The items method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for plant,types in plant_types.items():
    print(plant)
    print(types)

## 10. Finding the most common female names ##

top_female_names = []
for name, count in name_counts.items():
    if count == 2:
        top_female_names.append(name)
print(top_female_names)

## 11. Finding the most common male names ##

top_male_names = []
male_name_counts = {}
for item in legislators:
    if item[3] is "M" and item[7] > 1940:
        if item[1] in male_name_counts:
            male_name_counts[item[1]] += 1
        else:
            male_name_counts[item[1]] = 1

highest_male_count = None
for name, count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

for name, count in male_name_counts.items():
    if count is highest_male_count:
        top_male_names.append(name)

print(top_male_names)
## 2. Parsing the file ##

weather_data = []
a = open('la_weather.csv', "r")
data = a.read()
rows = data.split('\n')
for i in rows:
    temp = i.split(',')
    weather_data.append(temp)
print(weather_data[0:5])


## 3. Getting a single column from the data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for i in weather_data:
    weather.append(i[1])
print(weather[5])

## 4. Counting the items in a list ##

count = 0
for item in weather:
    count += 1
print(count)
print(len(weather))

## 6. Practice slicing lists ##

slice_me = [7,6,4,5,6]
slice1 = slice_me[2:4]
slice2 = slice_me[1:2]
slice3 = slice_me[3:5]

## 7. Removing the header ##

new_weather = weather[1:366]

## 8. The in statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals
print(cat_found)
print(space_monster_found)

## 9. Weather types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for wea in weather_types:
    test = wea in new_weather
    weather_type_found.append(test)
print(weather_type_found)
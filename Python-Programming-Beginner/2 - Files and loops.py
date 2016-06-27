## 2. Opening files ##

a = open("C:\Users\George varghese\Desktop\Analytics\DataQuest\Imp Links.txt", "r")
print(a)
f = open("C:\Users\George varghese\Desktop\Analytics\DataQuest\moviedata.csv", "r")

## 3. Reading in files ##

f = open("crime_rates.csv", "r")
data = f.read()
print(type(data))

## 4. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncan chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

## 6. Practice, loops ##

ten_rows = rows[0:10]
for i in ten_rows:
    print(i)

## 7. List of lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list[0])
    final_list.append(split_list[1])
print(final_list)


## 8. Practice, splitting elements in a list ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []
for i in rows:
    temp = i.split(',')
    final_data.append(temp)
print(final_data[0:5])

## 9. Accessing elements in a list of lists, the manual way ##

print(five_elements)
cities_list = []
for i in five_elements:
    cities_list.append(i[0])
print (cities_list)

## 10. Looping through a list of lists ##

crime_rates = []
cities_list = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the city name.
    crime_rates.append(crime_rate)
for row in final_data:
    cities_list.append(row[0])

## 11. Practice ##

f = open('crime_rates.csv', 'r')
data = f.read()
int_crime_rates = []
rows = data.split('\n')
print(rows[0:5])
for i in rows:
    temp = i.split(',')
    int_crime_rates.append(int(temp[1]))
print(int_crime_rates)
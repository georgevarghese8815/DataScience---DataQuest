## 3. Read the file into string ##

a = open('dq_unisex_names.csv', "r")
data = a.read()

## 4. Convert the string to a list ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split('\n')
print(data_list[0:5])

## 5. Convert the list of strings to a list of lists ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split('\n')
string_data = []
for i in data_list:
    temp = i.split(',')
    string_data.append(temp)
print(string_data[0:5])

## 6. Convert numerical values ##

print(string_data[0:5])
numerical_data = []
for i in string_data:
    temp = []
    name = i[0]
    numbr = float(i[1])
    temp.append(name)
    temp.append(numbr)
    numerical_data.append(temp)
print(numerical_data[0:5])

## 7. Filter the list ##

# The last value is ~100 people
numerical_data[len(numerical_data)-1]
thousand_or_greater = []
for i in numerical_data:
    if i[1] >= 1000:
        thousand_or_greater.append(i[0])
print(thousand_or_greater[0:10])


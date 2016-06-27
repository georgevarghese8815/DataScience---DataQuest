## 2. Sets ##

gender = []
for item in legislators:
    gender.append(item[3])
gender = set(gender)
print(gender)

## 3. Exploring the dataset ##

party = []
for item in legislators:
    party.append(item[6])
party = set(party)
print(party)
print(legislators[0:20])

## 4. Missing values ##

for item in legislators:
    if item[3] == "":
        item[3] = "M"

temp = []
for item in legislators:
    temp.append(item[3])

temp = set(temp)
print(temp)

## 5. Parsing birth years ##

birth_years = []
for item in legislators:
    parts = item[2].split("-")
    birth_years.append(parts[0])
print(birth_years[0:10])

## 6. Try/except blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float.")
print(Exception)

## 7. Exception instances ##

try:
    int("")
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The pass keyword ##

converted_years = []
for item in birth_years:
    year = item
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert birth years to integers ##

for item in legislators:
    temp = item[2].split("-")
    try:
        birth_year = int(temp[0])
    except Exception:
        birth_year = 0
    item.append(birth_year)
print(legislators[0:10])

## 10. Fill in years without a value ##

last_value = 1
for item in legislators:
    if item[7] == 0:
        item[7] = last_value
    last_value = item[7]
        
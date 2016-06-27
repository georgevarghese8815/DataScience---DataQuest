## 2. Lists of lists ##

import csv
a = open("world_alcohol.csv", "r")
b = csv.reader(a)
world_alcohol = list(b)
years = []
total = 0
for item in world_alcohol:
    years.append(item[0])
years = years[1:len(years)]
for item in years:
    total = total + float(item)
avg_year = total/len(years)

## 4. Using NumPy ##

import numpy as n
world_alcohol = n.genfromtxt("world_alcohol.csv", delimiter = ",")
print(world_alcohol)

## 5. Creating arrays ##

import numpy
vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

## 6. Array shape ##

vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
vector_shape = vector.shape
matrix_shape = matrix.shape

## 7. Data types ##

world_alcohol_dtype = world_alcohol.dtype

## 9. Reading in the data properly ##

import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", dtype = "U75", skip_header = True, delimiter = ",")
print(world_alcohol)

## 10. Indexing arrays ##

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]

## 11. Slicing arrays ##

countries = world_alcohol[:, 2]
alcohol_consumption = world_alcohol[:, 4]

## 12. Slicing one dimension ##

first_two_columns = world_alcohol[:, 0:2]
first_ten_years = world_alcohol[0:10, 0]
first_ten_rows = world_alcohol[0:10, :]

## 13. Slicing arrays ##

first_twenty_regions = world_alcohol[0:20, 1:3]
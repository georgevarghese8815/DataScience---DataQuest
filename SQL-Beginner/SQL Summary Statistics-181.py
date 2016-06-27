## 1. Counting in Python ##

import sqlite3 as s
conn = s.connect("factbook.db")
query = "Select * from facts;"
facts = conn.cursor().execute(query).fetchall()
print(facts)
facts_count = len(facts)

## 2. Counting in SQL ##

conn = sqlite3.connect("factbook.db")
query = "Select count(birth_rate) from facts;"
data = conn.cursor().execute(query).fetchall()
birth_rate_count = data[0][0]
print(type(data[0]))
print(type(data[0][0]))
print(birth_rate_count)

## 3. Min and max in SQL ##

conn = sqlite3.connect("factbook.db")
query1 = "Select Min(population_growth) from facts;"
query2 = "Select Max(death_rate) from facts;"
min_population_growth = conn.cursor().execute(query1).fetchall()[0][0]
max_death_rate = conn.cursor().execute(query2).fetchall()[0][0]
print(max_death_rate)
print(min_population_growth)


## 4. Sum and average in SQL ##

conn = sqlite3.connect("factbook.db")
query1 = "Select sum(area_land) from facts;"
query2 = "Select Avg(area_water) from facts;"
total_land_area = conn.cursor().execute(query1).fetchall()[0][0]
print(total_land_area)
avg_water_area = conn.cursor().execute(query2).fetchall()[0][0]
print(avg_water_area)

## 5. Multiple aggregation functions ##

conn = sqlite3.connect("factbook.db")
facts_stats = conn.execute("SELECT AVG(population), SUM(population), MAX(birth_rate) FROM facts;").fetchall()
print(facts_stats)

## 6. Conditional aggregation ##

conn = sqlite3.connect("factbook.db")
conn = sqlite3.connect("factbook.db")
pop_query = conn.execute("SELECT AVG(population_growth) FROM facts WHERE population > 10000000;").fetchall()
population_growth = pop_query[0][0]
print(population_growth)

## 7. Selecting unique rows ##

conn = sqlite3.connect("factbook.db")
unique_birth_rates = conn.execute("SELECT DISTINCT birth_rate FROM facts;").fetchall()
print(unique_birth_rates)

## 8. Distinct aggregations ##

conn = sqlite3.connect("factbook.db")
query1 = "Select Avg(Distinct birth_rate) from facts where population > 20000000"
average_birth_rate = conn.execute(query1).fetchall()[0][0]

query2 = "Select sum(distinct population) from facts where area_land > 1000000"
average_population = conn.execute(query2).fetchone()[0]

## 9. Arithemetic in SQL ##

conn = sqlite3.connect("factbook.db")
population_growth_millions = conn.execute("SELECT population_growth / 1000000.0 FROM facts;").fetchall()
print(population_growth_millions)

## 10. Arithemetic between columns ##

conn = sqlite3.connect("factbook.db")
next_year_population = conn.execute("SELECT population_growth * population + population FROM facts;").fetchall()
print(next_year_population)
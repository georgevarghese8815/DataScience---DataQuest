## 1. Introduction ##

c = conn.cursor()
query_plan_one  = c.execute("EXPLAIN QUERY PLAN Select * from facts where population > 1000000 and population_growth  < 0.5").fetchall()
print(query_plan_one)

## 2. Query plan for multi-column queries ##

import sqlite3
conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_idx on facts(population);").fetchall()
conn.execute("create index if not exists pop_growth_idx on facts(population_growth);").fetchall()

query_plan_two = conn.execute("explain query plan select * from facts where population > 1000000 and population_growth < 0.05;").fetchall()
print(query_plan_two)

## 5. Creating a multi-column index ##

conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_three = conn.execute("explain query plan select * from facts where population > 1000000 and population_growth < 0.05;").fetchall()
print(query_plan_three)

## 6. Covering index ##

query_plan_four = conn.execute("explain query plan select population, population_growth from facts where population > 1000000 and population_growth < 0.05;").fetchall()
print(query_plan_four)

## 7. Covering index for single column ##

query_plan_five = conn.execute("explain query plan select population from facts where population > 1000000;").fetchall()
print(query_plan_five)
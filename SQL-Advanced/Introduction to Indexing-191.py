## 3. Explain query plan ##

cursor = conn.cursor()
query_plan_one = cursor.execute("EXPLAIN QUERY PLAN select * from facts where area > 40000").fetchall()
query_plan_two = cursor.execute("EXPLAIN QUERY PLAN select area from facts where area > 40000").fetchall()
query_plan_three = cursor.execute('''EXPLAIN QUERY PLAN select * from facts where name = "Czech Republic"''').fetchall()
print(query_plan_one)
print(query_plan_two)
print(query_plan_three)

## 5. Time complexity ##

c = conn.cursor()
query_plan_four = c.execute("Explain Query Plan Select * from facts where id = 20").fetchall()
print(query_plan_four)

## 7. Indexing ##

india_index = conn.execute("select id from name_idx where name = 'India';").fetchall()[0][0]
print(india_index)

first_query_plan = conn.execute("explain query plan select id from name_idx where name = 'India';").fetchall()
print(first_query_plan)

india_row = conn.execute("select * from facts where id = ?;", (india_index,)).fetchall()
print(india_row)

second_query_plan = conn.execute("explain query plan select * from facts where id = ?;", (india_index,)).fetchall()
print(second_query_plan)

## 9. Query plan and indexing ##

query_plan_five = conn.execute("explain query plan SELECT population from facts WHERE name = 'India';").fetchall()
print(query_plan_five)

## 10. All together now ##

query_plan_six = conn.execute("explain query plan select * from facts where population > 10000 ;").fetchall()
print(query_plan_six)
conn.execute("create index if not exists pop_idx on facts(population)")
query_plan_seven = conn.execute("explain query plan select * from facts where population > 10000 ;").fetchall()
print(query_plan_seven)
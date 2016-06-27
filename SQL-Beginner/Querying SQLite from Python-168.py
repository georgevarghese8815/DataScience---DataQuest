## 3. Connect to the database ##

import sqlite3 as s
conn = s.connect("jobs.db")
print(type(conn))

## 6. Running a query ##

import sqlite3 as s
conn = s.connect("jobs.db")
cursor = conn.cursor()
print(type(cursor))

query = "Select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

query2 = "Select Major from recent_grads"
cursor.execute(query2)
majors = cursor.fetchall()
print(majors[0:2])

## 8. Fetching a specific number of results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "Select Major, Major_category from recent_grads"
cursor.execute(query)
five_results = cursor.fetchmany(5)

## 9. Closing the connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3 as s
conn = s.connect("jobs2.db")
cursor = conn.cursor()
query = "Select Major from recent_grads order by Major desc"
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
conn.close()
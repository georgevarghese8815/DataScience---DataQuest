## 2. Register DataFrame as a table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable("census2010")
tables = sqlCtx.tableNames()
print(tables)

## 3. Querying ##

query = "Select age from census2010"
sqlCtx.sql(query).show(20)


## 4. Filtering ##

query = 'select males,females from census2010 where age > 5 and age < 15'
sqlCtx.sql(query).show()

## 5. Mixing functionality ##

query = 'select males,females from census2010'
sqlCtx.sql(query).describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

df2 = sqlCtx.read.json('census_1980.json')
df3 = sqlCtx.read.json('census_1990.json')
df4 = sqlCtx.read.json('census_2000.json')

df2.registerTempTable('census1980')
df3.registerTempTable('census1990')
df4.registerTempTable('census2000')

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

query = """
 select census2010.total, census2000.total
 from census2010
 inner join census2000
 on census2010.age=census2000.age
"""

sqlCtx.sql(query).show(20)

## 8. SQL Functions ##

query = """
 select sum(census2010.total), sum(census2000.total), sum(census1990.total)
 from census2010
 inner join census2000
 on census2010.age=census2000.age
 inner join census1990
 on census2010.age=census1990.age
"""
sqlCtx.sql(query).show()
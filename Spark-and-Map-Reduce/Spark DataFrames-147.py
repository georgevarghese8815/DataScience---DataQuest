## 1. Spark DataFrame ##

with open('census_2010.json') as f:
    for i in range(0,4):
        print(f.readline())

## 2. Reading in data ##

# Import SQLContext
from pyspark.sql import SQLContext

# Pass in the SparkContext object `sc`
sqlCtx = SQLContext(sc)

# Read JSON data into DataFrame object `df`
df = sqlCtx.read.json("census_2010.json")

# Print the type
print(type(df))

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##

df.show(5)

## 5. Row object ##

first_five = df.head(5)
print(type(first_five))
for item in first_five:
    print(item.age)

## 6. Selecting columns ##

df[['age']].show()
df.select('age', 'males', 'females').show()

## 7. Filtering rows ##

fifty_plus = df[df.age > 5]
fifty_plus.show()

## 8. Comparing columns ##

df[df['females'] < df['males']].show()

## 9. Spark to Pandas ##

pandas_df = df.toPandas()
import matplotlib.pyplot as plt
plt.hist(pandas_df["total"])
plt.show()
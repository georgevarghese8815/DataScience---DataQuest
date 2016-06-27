import read
import collections
import operator
df = read.load_data()
headlines = ''
for index, row in df.iterrows():
    headlines = headlines + " " + str(row['headline'])
headlines = str.lower(headlines)
words = headlines.split() 
counts = dict(collections.Counter(words))
sorted_counts = sorted(counts.items(), key=operator.itemgetter(1),reverse=True)
for i in range(100):
    print(sorted_counts[i][0],str(sorted_counts[i][1]))
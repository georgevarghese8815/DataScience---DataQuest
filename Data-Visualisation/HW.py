import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# % matplotlib inline

hollywood_movies = pd.read_csv("C:\Users\George varghese\Desktop\Analytics\DataQuest\moviedata.csv")
print hollywood_movies.head(5)
hollywood_movies["exclude"].value_counts()
hollywood_movies = hollywood_movies.drop("exclude", axis = 1)
fig = plt.figure(figsize = (6, 10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.scatter(hollywood_movies["Profitability"], hollywood_movies["Audience Rating"])
ax1.set_xlabel("Profitability")
ax1.set_ylabel("Audience Rating")
ax1.set_title("Hollywood Movies, 2007-2011")
ax2.scatter(hollywood_movies["Audience Rating"], hollywood_movies["Profitability"])
ax2.set_ylabel("Profitability")
ax2.set_xlabel("Audience Rating")
ax2.set_title("Hollywood Movies, 2007-2011")
plt.show()
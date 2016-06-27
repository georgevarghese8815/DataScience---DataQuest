## 2. Authenticating with the API ##

header = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=header, params=params)
python_top = response.json()

## 3. Getting the most upvoted article ##

import pandas as pd
python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes = 0
for article in python_top_articles:
    ar = article["data"]
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]

data = pd.DataFrame(data = python_top_articles[0])

## 4. Getting article comments ##

response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u",headers=headers)
comments = response.json()

## 5. Getting the most upvoted comment ##

comments_list = comments[1]["data"]["children"]
most_upvoted_comment = ""
most_upvotes_comment = 0
for comment in comments_list:
    co = comment["data"]
    if co["ups"] >= most_upvotes_comment:
        most_upvoted_comment = co["id"]
        most_upvotes_comment = co["ups"]

## 6. Upvoting a comment ##

params = {"dir": 1, "id": "d16y4ry"}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.post("https://oauth.reddit.com/api/vote", json = params, headers = headers)
status = response.status_code
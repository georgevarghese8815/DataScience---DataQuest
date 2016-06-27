def load_data():
    import pandas as pd
    hn = pd.read_csv("hn_stories.csv")
    hn.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return hn

if __name__ == "__main__":
    load_data()
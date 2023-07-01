import pandas as pd

# Sample DataFrame
tweets_df = pd.DataFrame({
    'text': [
        'RT @user1: This is a retweet',
        'This is a regular tweet',
        'RT @user2: Another retweet',
        'RT @user3: Yet another retweet'
    ]
})

# Select retweets from the Twitter DataFrame: result
# Each time the x perameter takes the text column value and then check it is equal to the 'RT' or not.
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

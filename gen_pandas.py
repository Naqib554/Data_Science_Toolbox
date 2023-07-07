import pandas as pd

# Assuming you already have a DataFrame called df

# Create a DataFrame
data = {'created_at': ['2023-06-30 11:14:30', '2023-06-30 12:45:18', '2023-06-30 17:23:52']}
df = pd.DataFrame(data)
# print(df)
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry for entry in tweet_time if entry[2023]=='12']

# Print the extracted times
print(tweet_clock_time)

import pandas as pd

# Assuming you already have a DataFrame called df

# Create a DataFrame
data = {'created_at': ['2023-06-30 11:14:30', '2023-06-30 12:45:18', '2023-06-30 17:23:52']}
df = pd.DataFrame(data)

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# [:4] this represent the year 
# entry[11:13] this represent the hour
# if both condition are satisfied then the output expresion entry[11:19] is assigned to the tweet_clock_time.
# Extract the clock time for entries where the year is 2023 and the hour is 12: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[:4] == '2023' and entry[11:13] == '12']

# Print the extracted times
print(tweet_clock_time)

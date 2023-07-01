import pandas as pd
def count_entries(csv_file, c_size, colname):  
        
        # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    # If the chunksize is set to 10, it means that the pd.read_csv function
    # will read and process 10 rows of data at a time.
    # Each iteration of the loop will provide a chunk containing 10 rows from the CSV file.
    for chunk in pd.read_csv('E:\\Toolbox\\tweets.csv', chunksize=10):
            # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict:
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict
res=count_entries(csv_file='E:\\Toolbox\\tweets.csv', c_size=10, colname='language')
print(res)
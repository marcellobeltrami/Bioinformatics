import pandas as pd

import pandas as pd

# Read the text file
with open('system-logdad.txt', 'r') as file:
    lines = file.readlines()

# Split the lines into columns (assuming the text file is tab-separated)
data = [line.strip().split('\t') for line in lines]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Optionally, you can set column names if available
df.columns = ['INFO', 'Job_task', 'Date', "Time", "SC_location", "Repair__ID", "Message_output" ]

# Print the resulting DataFrame
print(df)





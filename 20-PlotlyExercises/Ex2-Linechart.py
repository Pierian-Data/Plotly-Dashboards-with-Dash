"""
Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
that plots seven days worth of temperature data on one graph.
You can use a for loop to assign each day to its own trace.
"""
# Perform imports here:




# Create a pandas DataFrame from mpg.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# Define a data variable
data = [{



} for day in days]

# Define the layout





# Create a fig from data and layout, and plot the fig

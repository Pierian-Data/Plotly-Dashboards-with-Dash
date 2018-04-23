#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:




# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']


# Use a for loop (or list comprehension to create traces for the data list)
data = []

for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter()
    data.append(trace)

# Define the layout





# Create a fig from data and layout, and plot the fig

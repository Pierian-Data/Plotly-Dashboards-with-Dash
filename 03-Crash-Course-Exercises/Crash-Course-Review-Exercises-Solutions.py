##################################################################
####### Crash Course Review Exercises - Solutions
#########################################################

#########################################################
# Complete the tasks numbered below.
# If you get stuck, check out the solution video!
#######################################################

#######
# TASK 1: Import pandas and numpy
######
import numpy as np
import pandas as pd


#######
# TASK 2: Set Numpy's random number generator seed to 101
######

np.random.seed(101)

#######
# TASK 3: Create a NumPy Matrix of 100 rows by 5 columns consisting of
#         random integers from 1-100. (Keep in mind that the upper
#         limit may be exclusive.)
######
mat = np.random.randint(1,101,(100,5))
print(mat)


#######
# TASK 4: Now use pd.DataFrame() to read in this numpy array as a dataframe.
#         Simple pass in the numpy array into that function to get back a
#         dataframe. Pandas will auto label the columns to 0-4
######

df = pd.DataFrame(mat)
print(df)

#######
# TASK 5: Using your previously created DataFrame, use [df.columns = [...]]
#         (https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas)
#         to rename the pandas columns to be ['f1','f2','f3','f4','label'].
######

df.columns = ['f1','f2','f3','f4','label']

#######
# TASK 6: Alright, all the other tasks were hopefully straightforward.
#         This final task will allow you to quickly check to see if you are at
#         the right level with pandas! Do the following:
#         Create a dataframe with the columns ['A','B','C','D'] with each column
#         having 50 rows of random numbers for data. The random numbers should be
#         between 0 and 100. (Hint: Use numpy to create the numbers, then pass
#         it in to pd.DataFrame(), check out the data= and index= parameters
#         for that call.)
random_numbers = np.random.randint(0,100,200)
random_mat = random_numbers.reshape(50,4)
col_names = 'A B C D'.split()
df = pd.DataFrame(data = random_mat,columns=col_names)

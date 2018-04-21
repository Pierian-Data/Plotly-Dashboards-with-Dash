############################
### Numpy Crash Course #####
############################
import numpy as np

my_list = [0,1,2,3,4]

arr = np.array(my_list)

print(arr)


# arange integers, takes in start,stop, and step size

a = np.arange(0,10)
print(a)

a= np.arange(0,10,2)
print(a)

# Create an array of zeros

a = np.zeros((5,5))
print(a)

# Create an array of ones

a = np.ones((2,4))
print(a)

# Create an array of random integers (uniform distribution between limits)

a = np.random.randint(0,10)
print(a)

# Create 2d matrix of random ints

a = np.random.randint(0,10,(3,3))
print(a)

# Create linearly spaced array
a = np.linspace(0,10,6)
print(a)


a = np.linspace(0,10,101)
print(a)

################################
#### Numpy Operations #########
##############################

# Setting a seed allows you to get the same "random" numbers that we do
# This is really nice for testing, so you can compare results
np.random.seed(101) # watch video for details
arr = np.random.randint(0,100,10)
print(arr)
# If you call this again, you will get a different set of random integers than
# the first time you called it. But both sets will be the same to someone else's
# who also ran these 2 calls immediately after setting the same seed.
arr2 = np.random.randint(0,100,10)
print(arr2)


# Simple operations

print(arr.max())

print(arr.min())

print(arr.mean())

# Index location of min
print(arr.argmin())

print(arr.argmax())

print(arr.reshape(2,5))

###########################
#### Indexing ############
#########################

# You can use .reshape() to change the shape of a 1d array to a 2d,3d, etc.. array
# Keep in mind, we will mainly be working with 2d tabular data.  
mat = np.arange(0,100).reshape(10,10)
print(mat)

row = 0
col = 1

# Selecting an individual number:
print(mat[row,col])

# Select an entire column (all row entries of this column "col")
print(mat[:,col])

# Select an entire column (all row entries of this column "col")
print(mat[row,:])


#######################
##### Masking #########
#######################
# Masking allows you to use conditional filters to grab elements
# we'll see this idea used in pandas.

print(mat > 50)


print(mat[mat>50])


# That is all for NumPy! NumPy is a really large library that does a lot
# more than what we showed here. But for our use cases in visualization, these
# are the basics we need to know for now. Later on we may introduce other
# NumPy concepts.

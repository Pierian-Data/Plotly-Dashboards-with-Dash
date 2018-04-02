
# coding: utf-8

# # Pandas Crash Course
# 
# We'll use numpy a lot more than pandas, but here is a quick taste in case you haven't seen it before.

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_csv('salaries.csv')


# In[3]:

df


# In[4]:

df['Name']


# In[5]:

df['Salary']


# In[6]:

df[['Name','Salary']]


# In[7]:

df['Age']


# In[8]:

df['Age'].mean()


# In[10]:

df['Age'] > 30


# In[11]:

age_filter = df['Age'] > 30


# In[12]:

df[age_filter]


# In[13]:

df[df['Age'] > 30]


# In[ ]:




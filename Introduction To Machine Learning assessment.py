#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pwd


# In[3]:


ls


# In[4]:


newfile = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv',encoding = 'latin 1')


# In[5]:


newfile


# In[6]:


newfile.shape


# In[7]:


newfile.groupby('Item').describe().head()


# In[8]:


newfile.groupby(['Item'])['Y2014','Y2017'].sum()


# In[9]:


newfile.describe()['Y2015']


# In[10]:


newfile.isnull()['Y2016'].sum()


# In[11]:


newfile['Y2016'].sum()


# In[12]:


(newfile.isnull()['Y2016'].sum())/(newfile['Y2016'].sum()) *100


# In[13]:


newfile.groupby(['Element Code'])['Y2014','Y2015','Y2016','Y2017','Y2018'].sum().sum()


# In[14]:


newfile.groupby(['Element'])['Y2014','Y2015','Y2016','Y2017','Y2018'].sum()


# In[15]:


newfile.groupby(['Element'])['Y2014'].sum()


# In[16]:


newfile.groupby(['Element'])['Element','Y2014'].sum()


# In[17]:


newfile.groupby(['Element','Area'])['Y2018'].sum()['Import Quantity']['Algeria']


# In[18]:


newfile['Area'].value_counts().count()


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[31]:


import seaborn as sns


from math import sqrt
from scipy import stats

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sns.load_dataset('tips')


# In[32]:


df= sns.load_dataset('tips')


# In[33]:


sns.distplot(df.total_bill)
plt.title('distribution of total bill')


# In[34]:


sns.distplot(df.tip)


# In[35]:


df.tip.mean(), df.tip.median()


# In[43]:


not_smokers = df[df.smoker != 'yes']


# In[45]:


μ = df.tip.mean()
xbar = not_smokers.tip.mean()
s = not_smokers.tip.std()
n = not_smokers.shape[0]


# In[46]:


degf = n - 1
standard_error = s / sqrt(n)

t = (xbar - μ) / (s / sqrt(n))
t


# there is no difference in the means of smokers and non smokers

# In[54]:


time= df[df.time!='dinner']


# In[55]:


μ = df.tip.mean()
xbar = time.tip.mean()
s = time.tip.std()
n = time.shape[0]


# In[56]:


degf = n - 1
standard_error = s / sqrt(n)

t = (xbar - μ) / (s / sqrt(n))
t


# there is no difference in the means of dinner and non dinner times.

# In[68]:


observed = df.total_bill


# In[69]:


chi2, p, degf, expected = stats.chi2_contingency(df.total_bill)

print('Observed\n')
print(observed.values)
print('---\nExpected\n')
print(expected)
print('---\n')
print(f'chi^2 = {chi2:.4f}')
print(f'p     = {p:.4f}')


# In[ ]:





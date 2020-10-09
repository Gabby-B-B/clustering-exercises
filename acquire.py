#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os

from env import host, user, password


# In[3]:


def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[6]:


sql_query = '''
SELECT * FROM properties_2017
JOIN airconditioningtype ON properties_2017.airconditioningtypeid= airconditioningtype.airconditioningtypeid
JOIN architecturalstyletype ON properties_2017.architecturalstyletypeid = architecturalstyletype.architecturalstyletypeid
JOIN heatingorsystemtype ON properties_2017.heatingorsystemtypeid = heatingorsystemtype.heatingorsystemtypeid
JOIN propertylandusetype ON properties_2017.propertylandusetypeid = propertylandusetype.propertylandusetypeid
JOIN predictions_2017 ON properties_2017.parcelid = predictions_2017.parcelid
LEFT JOIN buildingclasstype ON properties_2017.buildingclasstypeid = buildingclasstype.buildingclasstypeid
LEFT JOIN storytype ON properties_2017.storytypeid = storytype.storytypeid
LEFT JOIN typeconstructiontype ON properties_2017.typeconstructiontypeid = typeconstructiontype.typeconstructiontypeid
LEFT JOIN unique_properties ON properties_2017.parcelid = unique_properties.parcelid
WHERE transactiondate LIKE '2017-%%-%%'
AND WHERE longitude IS NOT NULL AND WHERE latitude IS NOT NULL;
            '''
df = pd.read_sql(sql_query, get_connection('zillow'))
df.to_csv('zillow_df.csv')
df.info()


# In[15]:


def get_zillow_data():
    filename = "zillow_df.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''SELECT * FROM properties_2017
JOIN airconditioningtype ON properties_2017.airconditioningtypeid= airconditioningtype.airconditioningtypeid
JOIN architecturalstyletype ON properties_2017.architecturalstyletypeid = architecturalstyletype.architecturalstyletypeid
JOIN heatingorsystemtype ON properties_2017.heatingorsystemtypeid = heatingorsystemtype.heatingorsystemtypeid
JOIN propertylandusetype ON properties_2017.propertylandusetypeid = propertylandusetype.propertylandusetypeid
JOIN predictions_2017 ON properties_2017.parcelid = predictions_2017.parcelid
LEFT JOIN buildingclasstype ON properties_2017.buildingclasstypeid = buildingclasstype.buildingclasstypeid
LEFT JOIN storytype ON properties_2017.storytypeid = storytype.storytypeid
LEFT JOIN typeconstructiontype ON properties_2017.typeconstructiontypeid = typeconstructiontype.typeconstructiontypeid
LEFT JOIN unique_properties ON properties_2017.parcelid = unique_properties.parcelid
WHERE transactiondate LIKE '2017-%%-%%'
AND WHERE longitude IS NOT NULL AND WHERE latitude IS NOT NULL; ''', get_connection('zillow'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)
        # Return the dataframe to the calling code
        return df


# In[13]:


df.info()


# In[19]:





# In[ ]:





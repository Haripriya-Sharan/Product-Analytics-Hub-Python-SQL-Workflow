#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[12]:


df1=pd.read_csv(r"C:\Users\Haripriya Sharan\Desktop\Headphones.csv\Headphones.csv")


# In[5]:


df1.head(20)


# In[8]:


df2= pd.read_csv(r"C:\Users\Haripriya Sharan\Desktop\Cameras.csv\Cameras.csv")


# In[9]:


df2.head(20)


# In[13]:


# Combine them
combined = pd.concat([df1, df2], ignore_index=True)

# Save to new CSV
combined.to_csv('combined.csv', index=False)


# In[14]:


df=pd.read_csv(r'combined.csv')


# In[85]:


df.head(20)


# In[38]:


df.drop(['image', 'link', 'main_category'], axis=1, inplace=True) #deleting the unnessary columns


# In[44]:


df.rename(columns={'sub_category':'category'})


# In[26]:


df = pd.read_csv('combined.csv',na_values=['FREE','Get'])
df['ratings'].unique()


# In[31]:


df['actual_price'] = df['actual_price'].replace({'₹': '', ',': ''}, regex=True).astype(float)


# In[32]:


df['discount_price'] = df['discount_price'].replace({'₹': '', ',': ''}, regex=True).astype(float)


# In[34]:


invalid_mask = pd.to_numeric(df['no_of_ratings'], errors='coerce').isna()
print(df[invalid_mask])


# In[46]:


df['no_of_ratings'] = (
    df['no_of_ratings']
    .astype(str)              # Ensure all values are strings
    .str.replace(',', '')     # Remove commas
)
df['no_of_ratings'] = pd.to_numeric(df['no_of_ratings'], errors='coerce')



# In[47]:


df['no_of_ratings'] = df['no_of_ratings'].fillna(0).astype(int)


# In[84]:


df


# In[51]:


print(df.columns.tolist())


# In[50]:


df = df.rename(columns={'sub_category': 'category'})


# In[75]:


print(df.dtypes)


# In[54]:


invalid_rows = df[df['discount_price'] > df['actual_price']]
print(invalid_rows)


# In[55]:


df['discount_percentage']=(df['actual_price']-df['discount_price'])/df['actual_price']*100


# In[57]:


df['discount_percentage']


# In[58]:


# Define bins and labels
bins = [0, 3, 4, 5]
labels = ['Low', 'Medium', 'High']

# Create a new column with binned rating categories
df['rating_bin'] = pd.cut(df['ratings'], bins=bins, labels=labels, right=False)


# In[62]:


df.head(20)


# In[61]:


df['discount_percentage'] = df['discount_percentage'].round(1)


# In[74]:


import numpy as np

# Find rows with NaN or inf values
mask = df['discount_price'].isna() | np.isinf(df['discount_price'])
print(df[mask])



# In[73]:


df = df[~(df['discount_price'].isna() | np.isinf(df['discount_price']))]
df['discount_price'] = df['discount_price'].astype(int)


# In[91]:


df['name'].is_unique




# In[81]:


duplicates = df[df['name'].duplicated(keep=False)]
print(duplicates)


# In[79]:


df = df.drop_duplicates(subset=['name'])


# In[92]:


pip install mysql-connector-python


# In[96]:


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:chandelier123@localhost:3306/mydatabase")
df.to_sql(name='df_project', con=engine, if_exists='replace', index=False)


# In[ ]:





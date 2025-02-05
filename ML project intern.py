#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


df=pd.read_csv("C:/Users/ankit maurya/Downloads/purchase_behaviour.CSV")


# In[3]:


df.head(5)


# In[4]:


df1=pd.read_csv("C:/Users/ankit maurya/Downloads/transaction_data.CSV")
df1.head(5)


# In[14]:


df1.TXN_ID.isnull().sum()


# In[15]:


df1.DATE.isnull().sum()


# In[17]:


df1.LYLTY_CARD_NBR.isnull().sum()


# In[18]:


df1.PROD_NAME.isnull().sum()


# In[19]:


df1.PROD_QTY.isnull().sum()


# In[20]:


df1.TOT_SALES.isnull().sum()


# In[5]:


merged_df = pd.merge(df, df1, on="LYLTY_CARD_NBR", how="inner")  # Use "inner" for matching records only


merged_df.head(5)


# In[6]:


top_products = merged_df.groupby("PROD_NAME")["TOT_SALES"].sum().nlargest(3)
print(top_products)


# In[24]:


loyal_customers = merged_df.groupby("LYLTY_CARD_NBR").size().reset_index(name="Purchase_Count")


# In[29]:


merged_df.LIFESTAGE.unique()


# In[8]:


loyal_customers = merged_df.groupby("LYLTY_CARD_NBR")["TXN_ID"].count().reset_index()


# In[9]:


loyal_customers.columns = ["LYLTY_CARD_NBR", "Total_Transactions"]


# In[10]:


loyal_customers = loyal_customers.merge(df[['LYLTY_CARD_NBR', 'LIFESTAGE', 'PREMIUM_CUSTOMER']], on="LYLTY_CARD_NBR", how="left").drop_duplicates()


# In[11]:


top_loyal_segments = loyal_customers.groupby(["LIFESTAGE", "PREMIUM_CUSTOMER"])["Total_Transactions"].sum().sort_values(ascending=False)


# In[12]:


print(top_loyal_segments.head(5))


# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
lifestages = ["Older Families", "Retirees", "Young Singles/Couples", "Young Families", "Older Singles/Couples"]
transactions = [23160, 21466, 20854, 19122, 18407]

# Plot
plt.figure(figsize=(10,5))
sns.barplot(x=lifestages, y=transactions, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("Lifestage")
plt.ylabel("Total Transactions")
plt.title("Most Loyal Customer Segments")
plt.show()


# In[14]:


import matplotlib.pyplot as plt

# Sample data
labels = ["Budget", "Mainstream", "Premium"]
values = [3, 2, 0]  # Based on counts from your dataset

# Plot
plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=["#66b3ff", "#99ff99", "#ffcc99"])
plt.title("Premium vs Budget Customer Distribution")
plt.show()


# In[15]:


products = ["Dorito Corn Chips Supreme 380g", "Smiths Crinkle Chips Original 380g", "Smiths Crinkle Chips Salt & Vinegar 330g"]
sales = [40352, 36367.6, 34804.2]

plt.figure(figsize=(10,5))
sns.barplot(x=sales, y=products, palette="coolwarm")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Name")
plt.title("Top 3 Most Profitable Products")
plt.show()


# In[16]:


import seaborn as sns

# Sample DataFrame
data = pd.DataFrame({
    "Lifestage": ["Older Families", "Retirees", "Young Singles/Couples", "Young Families", "Older Singles/Couples"],
    "Doritos Sales": [12000, 9000, 15000, 8000, 6000],
    "Smiths Original Sales": [10000, 11000, 9000, 8500, 7500],
    "Smiths Salt & Vinegar Sales": [9500, 10500, 8500, 7500, 7200]
})

plt.figure(figsize=(8,6))
sns.heatmap(data.set_index("Lifestage"), cmap="Blues", annot=True, fmt=".0f")
plt.title("Heatmap: Customer Segments vs. Preferred Products")
plt.show()


# In[ ]:





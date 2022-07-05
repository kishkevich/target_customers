# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import scipy.stats as st
#pd.set_option('display.max_columns', None)
import math
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set_style('whitegrid')
import missingno as msno
from sklearn.preprocessing import StandardScaler
from scipy import stats


data = pd.read_csv('clients.csv')


#print (data.shape)
#print (data.describe())
#print (data.info ())
#print (data.describe(include=['object', 'bool']))
#print (data.isnull().sum())

#print (data['source'].value_counts())


data.rename (columns = {"Year of sale":"Year_of_sale","Month of sale":"Month_of_sale","Type of property":"Type_of_property", "Property number":"Property_number", "Area (ft.)":"Area", "Customer ID":"Customer_ID",
        "Age at time of purchase":"Age_at_time_of_purchase","Age Interval":"Age_Interval" ,"Deal satisfaction":"Deal_satisfaction"},  inplace = True)
#print (data.head())

group_deal= data.groupby('Year_of_sale')["Deal_satisfaction"].sum().reset_index()
group_gender=data.groupby(["Year_of_sale","Gender"])["Age_at_time_of_purchase"].mean().reset_index()

plt.figure(figsize=(15, 10))
sns.barplot(x="Year_of_sale", y="Deal_satisfaction", data=group_deal)
plt.xticks(rotation=90);
plt.show()

plt.figure(figsize=(15, 10))
sns.barplot(x="Gender", y="Age_at_time_of_purchase", data=group_gender)
plt.xticks(rotation=90);
plt.show()

plt.figure(figsize=(15, 10))
sns.countplot(x="Age_at_time_of_purchase", data=data, order = data['Age_at_time_of_purchase'].value_counts().index)
plt.xticks(rotation=90);
plt.show()

sns.relplot(x="Country", y="Age_at_time_of_purchase",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=data)
plt.xticks(rotation=90);
plt.show()

data['Mortgage'] = data['Mortgage'].str.lower().replace({'yes': 1, 'no': 0})
plt.figure(figsize=(15, 10))
sns.barplot(x="Mortgage", y="Age_at_time_of_purchase", data=data)
plt.xticks(rotation=90);
plt.show()


sns.lineplot(data=data, x="Deal_satisfaction", y="Price", hue="Area")
plt.show()

sns.lineplot(data=data, x="Deal_satisfaction", y="Price", hue="Area")
plt.show()
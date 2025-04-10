#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 07:19:34 2025

@author: jovannamelissa
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('synthetic_insurance_data.csv')

data.info()
data.loc[data.duplicated()]
data.loc[data.isna().any(axis = 1)]

credit_score_cat = []

for i in data['Credit_Score']:
    if i >= 770:
        category = 'High'
    elif i >= 500 and i < 770:
        category = 'Fair'
    elif i < 500:
        cateogry = 'Low'
    credit_score_cat.append(category)
    
credit_score_cat = pd.Series(credit_score_cat)
data['credit_series_category'] = credit_score_cat

cat_graph = data.groupby(['credit_series_category']).size()
cat_graph.plot.bar(color = 'green')
plt.xlabel('Credit Score Category')
plt.show()

plt.hist(data['Premium_Amount'], bins=10, edgecolor ="black")
plt.xlabel("Premium Amount Range")
plt.ylabel("Frequency")
plt.title("Histogram of Premium Amount Count")
plt.show()

data.to_csv('insurance_data_cleaned.csv', index = True)

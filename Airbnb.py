#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:23:03 2017

@author: qlwang
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir("/Users/qlwang/Desktop/airbnb_kaggle/")

sns.set_style("white", {'ytick.major.size': 10.0})
sns.set_context("poster", font_scale=1.1)

# Load the data into DataFrames
train_users = pd.read_csv('train_users_2.csv')
test_users = pd.read_csv('test_users.csv')

print "We have", train_users.shape[0], "users in the training set and", test_users.shape[0], "in the test set."
print "In total we have", train_users.shape[0] + test_users.shape[0], "users." 
                                           
# Merge train and test users
users = pd.concat((train_users, test_users), axis=0, ignore_index=True)

# Remove ID's since now we are not interested in making predictions
users.drop('id',axis=1, inplace=True)

users.head()

# Missing Data
users.gender.replace('-unknown-', np.nan, inplace=True)
users_nan = (users.isnull().sum() / users.shape[0]) * 100
print users_nan
users_nan[users_nan > 0].drop('country_destination')

print "Just for the sake of curiosity; we have", int(train_users.date_first_booking.isnull().sum() / float(train_users.shape[0]) * 100), "% of missing values at date_first_booking in the training data"

users.age.describe()

print(sum(users.age > 122))
print(sum(users.age < 18)

users.loc[users.age > 95, 'age'] = np.nan
users.loc[users.age < 13, 'age'] = np.nan
         
# Data Types 

categorical_features = [
    'affiliate_channel',
    'affiliate_provider',
    'country_destination',
    'first_affiliate_tracked',
    'first_browser',
    'first_device_type',
    'gender',
    'language',
    'signup_app',
    'signup_method'
]

for categorical_feature in categorical_features:
    users[categorical_feature] = users[categorical_feature].astype('category')

users['date_account_created'] = pd.to_datetime(users['date_account_created'])
users['date_first_booking'] = pd.to_datetime(users['date_first_booking'])
users['date_first_active'] = pd.to_datetime((users.timestamp_first_active // 1000000), format='%Y%m%d')




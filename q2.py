# Question 2: 
# [10 marks] [CO1/PO3/C5]
# It is required to demonstrate on how to extract and analyze the csv data 
# from Kaggle <https://www.kaggle.com/ghoshsaptarshi/av-genpact-hack-dec2018?select=meal_info.csv>

import pandas as pd
import numpy as np

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

train_dat = pd.read_csv("/kaggle/input/av-genpact-hack-dec2018/train.csv")
train_dat.head()
train_dat.describe()

test_dat = pd.read_csv("/kaggle/input/av-genpact-hack-dec2018/test.csv")
test_dat.head()
test_dat.describe()

meal_info_dat = pd.read_csv("/kaggle/input/av-genpact-hack-dec2018/meal_info.csv")
meal_info_dat.head()
test_dat.describe()

center_info_dat = pd.read_csv('/kaggle/input/av-genpact-hack-dec2018/fulfilment_center_info.csv')
center_info_dat.head()
center_info_dat.describe()


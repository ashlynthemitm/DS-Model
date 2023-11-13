"""
Created on Mon Nov 13 18:22:01 2023

@author: Ashlyn Campbell
"""

import pandas as pd
from pandas import DataFrame, Series

df_school = pd.read_csv('DS-Model/data_raw/diversity_school.csv', sep=',')

print(df_school.head())
"""
Created on Mon Nov 13 18:22:01 2023

@author: Ashlyn Campbell
"""

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

df = pd.read_csv('DS-Model/data_raw/diversity_school.csv', sep=',')

# view the preprocessing tips & tricks howto_preprocess.txt

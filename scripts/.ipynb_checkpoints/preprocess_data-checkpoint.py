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


# Add Regions to Diversity_School dataset
def addRegions():
    # 4 Major Regions
    # States in the Northeast
    northeast_states = {'Connecticut', 'Delaware', 'Maine', 'Maryland', 'Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania', 'Rhode Island', 'Vermont'}

    # States in the Midwest
    midwest_states = {'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin'}

    # States in the South
    south_states = {'Alabama', 'Arkansas', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia'}

    # States in the West
    west_states = {'Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Oregon', 'Utah', 'Washington', 'Wyoming'}
    
    df = pd.read_csv('DS-Model/data_raw/diversity_school.csv', sep=',')

    
    for index, row in df.iterrows():
        current_region = ''
        if df.at[index,'state'] in northeast_states:
            current_region = 'northeast'
        elif df.at[index,'state'] in midwest_states:
            current_region = 'midwest'
        elif df.at[index,'state'] in south_states:
            current_region = 'south'
        elif df.at[index,'state'] in west_states:
            current_region = 'west'
        else:
            current_region = 'unknown'  
            
        df.at[index, 'region'] = current_region

        df.to_csv('DS-Model/data_raw/diversity_school.csv', index=False)

#addRegions()
# Now delete all rows with unknown regions
def cleanDiversitySchool():
    df = pd.read_csv('DS-Model/data_raw/diversity_school.csv', sep=',')
    print('Count of cells BEFORE dropping empty cells:', df.size, '\n')
    for index, row in df.iterrows():
        if df.at[index,'region'] == 'unknown':
            df = df.drop(index)
    df.dropna()
    df.to_csv('DS-Model/data_raw/diversity_school.csv', index=False)
    print('Count of cells AFTER dropping empty cells:', df.size, '\n')
# cleanDiversitySchool()

def addDiversityPercent():
    df = pd.read_csv('DS-Model/data_raw/diversity_school.csv', sep=',')
    
    for index, row in df.iterrows():
        diversity_percent = df.at[index, 'enrollment'] / df.at[index, 'total_enrollment']
            
        df.at[index,'diversity_percent'] = diversity_percent
    
    df.to_csv('DS-Model/data_raw/diversity_school.csv', index=False)
    
addDiversityPercent()
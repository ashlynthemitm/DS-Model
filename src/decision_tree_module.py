"""
Created on Mon Nov 25 23:20:01 2023

@author: Ashlyn Campbell
"""
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
default_folder = 'C:/Users/ashly/OneDrive/Documents/Education Material/FundamentalsDS/Project/DS-Model'

# Change the working directory
os.chdir(default_folder)

'''
The Six Figure Salary Predictive Model based on School Choice (Classification)
Target Feature: Six Figure Salary by mid-career (True or False)
Descriptive features: School Name, Stem Percent, Total_Cost of School, Rank of School, Diversity Index 
'''

def temp_name(file_path):
    df = pd.read_csv(file_path, sep=',')

    # seaborn styling
    sns.set(style='ticks')
    sns.pairplot(df, hue='name')

    # evenly distributed data can use bar graphs
    df['name'].value_counts().plot(kind='bar')
    df['stempercent'].value_counts().plot(kind='bar')
    
    # uneven distribution may be better with histogram
    df['rank'].plot.hist(bins=10)
    df['diversity_index'].plot.hist(bins=10)
    df['total_cost'].plot.hist(bins=10)
    
    # styling and plotting 
    sns.set(style='whitegrid', context='notebook')
    cols = ['rank', 'diversity_index', 'total_cost']
    sns.pairplot(df, hue='TrainingName', heigh=2.0)
    plt.show()
    
file_path = 'data_processed/modelling_data.csv'
temp_name(file_path)
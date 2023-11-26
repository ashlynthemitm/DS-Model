"""
Created on Mon Nov 24 21:47:01 2023
This module creates pie charts representing the diversity index in each region.
This will help us view the regions to look more towards with a diversity index
for either each region or directly towards specific states or concentrated 
schools.

@author: Ashlyn Campbell
"""
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def CreateDiversityPieChart(file_path):
    # Define dictionaries for diversity data in different regions
    northeast_diversity = {'Women': 0, 'American Indian / Alaska Native': 0, 'Asian': 0, 'Black': 0,'Hispanic': 0, 'Native Hawaiian / Pacific Islander': 0, 'White': 0,'Two Or More Races': 0, 'Unknown': 0, 'Non-Resident Foreign': 0,'Total Minority': 0}
    
    midwest_diversity = {'Women': 0, 'American Indian / Alaska Native': 0, 'Asian': 0, 'Black': 0,'Hispanic': 0, 'Native Hawaiian / Pacific Islander': 0, 'White': 0,'Two Or More Races': 0, 'Unknown': 0, 'Non-Resident Foreign': 0,'Total Minority': 0}
    
    west_diversity = {'Women': 0, 'American Indian / Alaska Native': 0, 'Asian': 0, 'Black': 0,'Hispanic': 0, 'Native Hawaiian / Pacific Islander': 0, 'White': 0,'Two Or More Races': 0, 'Unknown': 0, 'Non-Resident Foreign': 0,'Total Minority': 0}
    
    south_diversity = {'Women': 0, 'American Indian / Alaska Native': 0, 'Asian': 0, 'Black': 0, 'Hispanic': 0, 'Native Hawaiian / Pacific Islander': 0, 'White': 0,'Two Or More Races': 0, 'Unknown': 0, 'Non-Resident Foreign': 0,'Total Minority': 0}
    
    num_northeast_schools = 0
    num_midwest_schools = 0
    num_west_schools = 0
    num_south_schools = 0
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, sep=',')

    # Add diversity percentages and count schools in each region
    for index, row in df.iterrows():
        category = df.at[index, 'category']
        region = df.at[index, 'region']
        
        match region:
            case 'northeast':
                num_northeast_schools += 1
                northeast_diversity[category] += df.at[index, 'diversity_percent']
            case 'midwest':
                num_midwest_schools += 1
                midwest_diversity[category] += df.at[index, 'diversity_percent']
            case 'west':
                num_west_schools += 1
                west_diversity[category] += df.at[index, 'diversity_percent']
            case 'south':
                num_south_schools += 1
                south_diversity[category] += df.at[index, 'diversity_percent']
            case _:
                print(f'Something went wrong at index: {index}')
                
    # Normalize the counts to get percentages
    num_northeast_schools /= 10
    num_midwest_schools /= 10
    num_west_schools /= 10
    num_south_schools /= 10
        
    for key in northeast_diversity.keys():
        northeast_diversity[key] /= num_northeast_schools
        midwest_diversity[key] /= num_midwest_schools
        west_diversity[key] /= num_west_schools
        south_diversity[key] /= num_south_schools

    # Plot pie charts for each region
    def plot_pie_chart(region, title):
        labels = list(region.keys())
        sizes = list(region.values())
        colors = ['#87CEEB', '#FF7F50', '#32CD32', '#DC143C', '#8A2BE2', '#A0522D', '#E6E6FA', '#FFD700', '#BDB76B', '#00008B', '#FFFF00']
        plt.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, labeldistance=1.1)
        plt.legend(labels, loc='upper right', bbox_to_anchor=(1.15, 1.15))
        plt.axis('equal')
        plt.title(title)
        plt.gcf().set_size_inches(8, 8)
        plt.show()

    plot_pie_chart(northeast_diversity, 'Northeast Diversity Index')
    plot_pie_chart(midwest_diversity, 'Midwest Diversity Index')
    plot_pie_chart(west_diversity, 'West Diversity Index')
    plot_pie_chart(south_diversity, 'South Diversity Index')

    plt.close()

file_path = 'DS-Model/data_raw/diversity_school.csv'
CreateDiversityPieChart(file_path)

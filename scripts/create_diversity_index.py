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

def CreateDiversityPieChart():
  
    northeast_diversity = {
        'Women': 0,
        'American Indian / Alaska Native': 0,
        'Asian': 0,
        'Black': 0,
        'Hispanic': 0,
        'Native Hawaiian / Pacific Islander': 0,
        'White': 0,
        'Two Or More Races': 0,
        'Unknown': 0,
        'Non-Resident Foreign': 0,
        'Total Minority': 0
    }
    midwest_diversity = {
        'Women': 0,
        'American Indian / Alaska Native': 0,
        'Asian': 0,
        'Black': 0,
        'Hispanic': 0,
        'Native Hawaiian / Pacific Islander': 0,
        'White': 0,
        'Two Or More Races': 0,
        'Unknown': 0,
        'Non-Resident Foreign': 0,
        'Total Minority': 0
    }
    west_diversity = {
        'Women': 0,
        'American Indian / Alaska Native': 0,
        'Asian': 0,
        'Black': 0,
        'Hispanic': 0,
        'Native Hawaiian / Pacific Islander': 0,
        'White': 0,
        'Two Or More Races': 0,
        'Unknown': 0,
        'Non-Resident Foreign': 0,
        'Total Minority': 0
    }
    south_diversity = {
        'Women': 0,
        'American Indian / Alaska Native': 0,
        'Asian': 0,
        'Black': 0,
        'Hispanic': 0,
        'Native Hawaiian / Pacific Islander': 0,
        'White': 0,
        'Two Or More Races': 0,
        'Unknown': 0,
        'Non-Resident Foreign': 0,
        'Total Minority': 0
    }
    
    num_northeast_schools = 0
    num_midwest_schools = 0
    num_west_schools = 0
    num_south_schools = 0
    
    df = pd.read_csv('DS-Model/data_raw/diversity_school.csv', sep=',')

    # add each of the diversity_percentages then divide by num schools in that region
    for index, row in df.iterrows():
        category = df.at[index,'category']
        match(df.at[index,'region']):
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
                f'Something went wrong at index: {index}'
                
    num_northeast_schools /= 10
    num_midwest_schools /= 10
    num_west_schools /= 10
    num_south_schools /= 10
        
    for key in northeast_diversity.keys():
        northeast_diversity[key] /= num_northeast_schools
        midwest_diversity[key] /= num_midwest_schools
        west_diversity[key] /= num_west_schools
        south_diversity[key] /= num_south_schools

    # print(f'Northeast: {northeast_diversity}')
    # print(f'Midwest: {midwest_diversity}')
    # print(f'West: {west_diversity}')
    # print(f'South: {south_diversity}')
        
    # combined_data = {key: northeast_diversity[key] + midwest_diversity[key] + west_diversity[key] + south_diversity[key] for key in northeast_diversity}
    
    
    # Northeast Diversity Pie Charts
    labels = list(northeast_diversity.keys())
    sizes = list(northeast_diversity.values())
    colors = ['#87CEEB', '#FF7F50', '#32CD32', '#DC143C', '#8A2BE2', '#A0522D', '#E6E6FA', '#FFD700', '#BDB76B', '#00008B', '#FFFF00']
    plt.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, labeldistance=1.1)
    plt.legend(labels, loc='upper right', bbox_to_anchor=(1.15, 1.15))
    plt.axis('equal')
    plt.title('Northeast Diversity Index')
    plt.gcf().set_size_inches(8, 8)
    # plt.savefig('DS-Model/visualizations/northeast_diversity.png')
    plt.show()

    # Midwest Diversity Pie Charts
    labels = list(midwest_diversity.keys())
    sizes = list(midwest_diversity.values())
    colors = ['#87CEEB', '#FF7F50', '#32CD32', '#DC143C', '#8A2BE2', '#A0522D', '#E6E6FA', '#FFD700', '#BDB76B', '#00008B', '#FFFF00']
    plt.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, labeldistance=1.1)
    plt.legend(labels, loc='upper right', bbox_to_anchor=(1.15, 1.15))
    plt.axis('equal')
    plt.title('Midwest Diversity Index')
    plt.gcf().set_size_inches(8, 8)
    # plt.savefig('DS-Model/visualizations/midwest_diversity.png')
    plt.show()
        
    # West Diversity Pie Charts
    labels = list(west_diversity.keys())
    sizes = list(west_diversity.values())
    colors = ['#87CEEB', '#FF7F50', '#32CD32', '#DC143C', '#8A2BE2', '#A0522D', '#E6E6FA', '#FFD700', '#BDB76B', '#00008B', '#FFFF00']
    plt.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, labeldistance=1.1)
    plt.legend(labels, loc='upper right', bbox_to_anchor=(1.15, 1.15))
    plt.axis('equal')
    plt.title('West Diversity Index')
    plt.gcf().set_size_inches(8, 8)
    # plt.savefig('DS-Model/visualizations/west_diversity.png')
    plt.show()
    
    # South Diversity Pie Charts
    labels = list(south_diversity.keys())
    sizes = list(south_diversity.values())
    colors = ['#87CEEB', '#FF7F50', '#32CD32', '#DC143C', '#8A2BE2', '#A0522D', '#E6E6FA', '#FFD700', '#BDB76B', '#00008B', '#FFFF00']
    plt.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=140, labeldistance=1.1)
    plt.legend(labels, loc='upper right', bbox_to_anchor=(1.15, 1.15))
    plt.axis('equal')
    plt.title('South Diversity Index')
    plt.gcf().set_size_inches(8, 8)
    # plt.savefig('DS-Model/visualizations/south_diversity.png')
    plt.show()
    
    plt.close()
    
CreateDiversityPieChart()
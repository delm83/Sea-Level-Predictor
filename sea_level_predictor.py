import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    #without this the legend produces duplicates
    fig, ax = plt.subplots()

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df, label='recorded sea level')
 
    # Create first line of best fit
    res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # Create new year series for x axis to extend years to 2050
    extended_years = pd.Series([year for year in range(1880, 2051)])
    plt.plot(extended_years, res.intercept + res.slope*extended_years, 'g', label='prediction line of best fit 1880 - 2050')
    
    # Create second line of best fit
    # Use only data from 2000
    df_recent = df[df['Year']>1999]
    res = linregress(x=df_recent['Year'], y=df_recent['CSIRO Adjusted Sea Level'])
    # Use only a series of years from 2000 - 2050
    recent_years = extended_years[extended_years>1999]
    plt.plot(recent_years, res.intercept + res.slope*recent_years, 'r', label='prediction line of best fit 2000 - 2050')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.tight_layout()
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)
 
    # Create first line of best fit
    res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(df.Year, res.intercept + res.slope*df.Year, 'g')
    
    # Create second line of best fit

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.tight_layout()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
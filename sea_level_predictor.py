import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,10))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_axis = list(range(1880,2050))
    y_axis = get_slope(slope, intercept, x_axis)

    plt.plot(x_axis, y_axis, color='r',label = 'Best Fit line 1')

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

def get_slope(slope, intercept, x_axis):
  y_axis = []
  for i, x in enumerate(x_axis):
      y_axis.append(slope*x_axis[i] + intercept)

  return y_axis

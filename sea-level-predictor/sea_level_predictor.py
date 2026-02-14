import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
    x = range(df.Year.tolist()[0], 2050)
    plt.plot(x, intercept + slope * x, color="black")
    # Create second line of best fit
    df = df[df.Year >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
    x = range(2000, 2050)
    plt.plot(x, intercept + slope * x, color="red")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
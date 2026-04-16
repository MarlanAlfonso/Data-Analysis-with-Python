import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Load the data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create the scatter plot
    fig, ax = plt.subplots(figsize=(16, 6))

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level'],
        color='steelblue',
        alpha=0.6,
        label='Observed data'
    )

    # 3. Line of best fit using ALL data (1880 to 2050)
    # linregress returns slope, intercept, r_value, p_value, std_err
    slope_all, intercept_all, _, _, _ = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Extend x-axis from first year in data all the way to 2050
    x_all = pd.Series(range(df['Year'].min(), 2051))
    y_all = slope_all * x_all + intercept_all

    ax.plot(
        x_all,
        y_all,
        color='red',
        linewidth=2,
        label='Best fit line (1880-2050)'
    )

    # 4. Line of best fit using data from 2000 onwards only
    df_recent = df[df['Year'] >= 2000]

    slope_recent, intercept_recent, _, _, _ = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    # Extend from year 2000 to 2050
    x_recent = pd.Series(range(2000, 2051))
    y_recent = slope_recent * x_recent + intercept_recent

    ax.plot(
        x_recent,
        y_recent,
        color='green',
        linewidth=2,
        label='Best fit line (2000-2050)'
    )

    # 5. Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return ax
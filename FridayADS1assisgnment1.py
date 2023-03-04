# Importint the Libraries

import pandas as pd
import matplotlib.pyplot as plt

# Reading the data into DataFrame

gdp_per_capita_scan = pd.read_csv('GDP_per_capita_scan.csv', index_col=0)

gdp_year = ['2015', '2016', '2017', '2018,', '2019']

def line_plot(gdp_per_capita_scan):
    """
    Creates a line plot showing the trends in the data over time.

    :param df: a pandas DataFrame containing the data to be plotted
    """
    # Set the figure size
    plt.figure(figsize=(10, 6))

    # Plot each country's data as a separate line
    for column in gdp_per_capita_scan.columns[:]:
        plt.plot(gdp_year, gdp_per_capita_scan[column], label=column)

    # Add titles and labels
    plt.title('GDP per capita for FINLAND NORWAY & SWEDEN')
    plt.xlabel('Year')
    plt.ylabel('GDP Per Capita ( US $)')
    plt.legend()

    # Show the plot
    plt.show()

line_plot(gdp_per_capita_scan)
    
# 2. Bar plot
def bar_plot(gdp_per_capita_scan, year):
    """
    Creates a bar plot comparing the values for each country in a given year.

    :param df: a pandas DataFrame containing the data to be plotted
    :param year: an integer specifying the year to plot
    """
    # Set the figure size
    plt.figure()

    # Get the data for that year
    data = gdp_per_capita_scan.loc[year]
    # Plot the data as a bar chart
    plt.bar(data.index, data.values)

    # Add titles and labels
    plt.title('GDP Per Capita by Scandinavian Country in {}'.format(year))
    plt.xlabel('Country')
    plt.ylabel('GDP Per Capita ( US $)')

    # Show the plot
    plt.show()

bar_plot(gdp_per_capita_scan, 2019)


# 3. Scatter plot
def scatter_plot(gdp_per_capita_scan):
    """
    Creates a scatter plot comparing the values for two countries across all years.

    :param df: a pandas DataFrame containing the data to be plotted
    """
    # Set the figure size
    plt.figure(figsize=(10, 6))

    # Choose two countries to plot
    country1 = 'Norway'
    country2 = 'Sweden'

    # Plot the data as a scatter chart
    plt.scatter(gdp_per_capita_scan[country1], gdp_per_capita_scan[country2])

    # Add titles and labels
    plt.title('Comparing GDP of {} vs {} across years'.format(country1, country2))
    plt.xlabel(country1)
    plt.ylabel(country2)

    # Show the plot
    plt.show()

scatter_plot(gdp_per_capita_scan)

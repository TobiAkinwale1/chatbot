import matplotlib.pyplot as plt
import pandas as pd

def plot_city_trends(file_path, selected_cities):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Filtering the dataset for the selected cities
    filtered_data = data[data['RegionName'].isin(selected_cities)]

    # Setting the index to RegionName for easier slicing
    filtered_data.set_index('RegionName', inplace=True)

    # Dropping non-date columns for clearer plots
    date_columns = filtered_data.columns[4:]  # Assuming first four columns are non-date
    trend_data = filtered_data[date_columns]

    # Plotting the trends
    plt.figure(figsize=(14, 8))
    for city in selected_cities:
        plt.plot(trend_data.columns, trend_data.loc[city], label=city)

    plt.title('Trend of Median Sale Prices in Major US Metropolitan Areas (2018-2024)')
    plt.xlabel('Month-Year')
    plt.ylabel('Median Sale Price ($)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()



# Example usage
#plot_city_trends('median_zillow.csv', ['New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Dallas, TX'])

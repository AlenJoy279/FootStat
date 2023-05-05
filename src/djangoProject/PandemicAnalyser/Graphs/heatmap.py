import os
import re
import geopandas as gpd
import mpld3
import pandas as pd
import matplotlib.pyplot as plt
import pycountry as pycountry
import matplotlib.colors as colors


def combine_jsonl(path):
    # Function to create a merged csv of monthly tweets for heatmap
    base = path
    files = os.listdir(path)
    df = pd.read_json(f'{base}/{files[0]}', lines=True, orient='records')
    concat_df = [df]

    print(files)

    for j in range(1, len(files)):
        dfs = pd.read_json(f'{base}/{files[j]}', lines=True, orient='records')
        concat_df.append(dfs)
        print(f'{base}/{files[j]}')

    print(len(concat_df))

    result = pd.concat(concat_df, ignore_index=True)

    # Keeping only the columns necessary for heatmap
    result = result[['created_at', 'id', 'place']]

    # Drop any rows with any NaN
    result = result.dropna(how='any')

    # Remove everything but country from the place column
    result['place'] = result['place'].apply(filter_country)

    basename = base.split('/')[-1]
    fname = "F:/ca400/hydrated_combined_monthly/"

    result.to_csv(f'{fname}{basename}.csv')
    print(f'{fname}{basename}.csv')


def filter_country(row):
    # Function to filter out any data in the "place" column that is not the name of the country
    row = str(row)
    # Match 'country' followed by a colon and zero or more spaces, followed by a single- or double-quoted string
    # containing the country name
    pattern1 = r"'country':\s*('[^']*'|\"[^\"]*\")"
    match1 = re.search(pattern1, row)
    if match1:
        # Extract the country name and remove all quotes
        country_name = match1.group(1).strip("'\"")
        return f"{country_name}"

    # Match 'country' followed by a colon and one or more spaces, followed by an empty-quoted string and a country
    # name in double quotes
    pattern2 = r"'country':\s*\"\"([^\"]*)\"\""
    match2 = re.search(pattern2, row)
    if match2:
        # Extract the country name and remove all quotes
        country_name = match2.group(1).strip("'\"")
        return f"{country_name}"

    return ""


def get_tweet_heatmap(path_to_csv):

    # Example use: get_tweet_heatmap("F:/ca400/hydrated_combined_monthly/2020_07.csv")
    df_path = path_to_csv
    basename = df_path.split("/")[-1]
    df = pd.read_csv(df_path)
    country_counts = df['place'].value_counts()

    # Replace country names to match with pycountry db
    country_counts = country_counts.rename({'The Netherlands': 'Netherlands'})
    country_counts = country_counts.rename({'Republic of the Philippines': 'Philippines'})
    country_counts = country_counts.rename({r"People's Republic of China": 'China'})
    country_counts = country_counts.rename({r'Kingdom of Saudi Arabia': 'Saudi Arabia'})
    country_counts = country_counts.rename({'Republic of Korea': 'South Korea'})
    country_counts = country_counts.rename({'Russia': 'Russian Federation'})
    country_counts = country_counts.rename({'Democratic Republic of Congo': 'Congo, The Democratic Republic of the'})
    country_counts = country_counts.rename({'Congo Brazzaville': 'Republic of the Congo'})
    country_counts = country_counts.rename({'Sint Maarten': 'Sint Maarten (Dutch part)'})
    country_counts = country_counts.rename({'Ivory Coast': f"Côte d'Ivoire"})
    country_counts = country_counts.rename({'Vatican City': 'Holy See (Vatican City State)'})
    country_counts = country_counts.rename({'La Réunion': 'Réunion'})
    country_counts = country_counts.rename({'Cape Verde': 'Cabo Verde'})
    country_counts = country_counts.rename({'Saint Martin': 'Saint Martin (French part)'})

    # Convert country names to iso_a3 format
    for country_name in country_counts.index:
        try:
            country = pycountry.countries.get(name=country_name)
            if country is None:
                country = pycountry.countries.get(common_name=country_name)
                if country is None:
                    country = pycountry.countries.get(official_name=country_name)
            iso_a3 = country.alpha_3
        except AttributeError:
            iso_a3 = 'Unknown'
        country_counts.rename(index={country_name: iso_a3}, inplace=True)

    # Print the country counts
    #print(country_counts)

    # Load the world map shapefile into a geopandas GeoDataFrame
    world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge the country counts data with the world map GeoDataFrame using ISO country codes
    merged_data = world_map.merge(country_counts, how='left', left_on='iso_a3', right_index=True)

    # Fill any missing country count values with zero
    merged_data['place'].fillna(0, inplace=True)

    # Define the custom interval boundaries
    interval_bounds = [0, 1, 10, 50, 200, 400, 800, 1000, 1500, 2000, 4000, 8000, 15000, 20000]

    # Define the custom color map
    custom_colors = ['#eaeaea', '#ffffff', '#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5',
                      '#1b67a7', '#165993', '#115087', '#104994', '#084594']
    # custom_cmap = colors.ListedColormap(custom_colors)
    custom_norm = colors.BoundaryNorm(interval_bounds, len(custom_colors))

    # Plot the choropleth map using the merged data with custom color scaling
    fig, ax = plt.subplots(figsize=(14, 10))
    merged_data.plot(column='place', cmap='PuBu', linewidth=0.8, edgecolor='0.8', ax=ax,
                     legend=True,
                     legend_kwds={'label': 'Monthly Tweet Frequency', 'orientation': 'horizontal'})
    ax.axis('off')
    ax.set_title(f'{basename.split(".")[0]}')

    html = mpld3.fig_to_html(fig)
    centered_html = f'<div style="text-align: center;">{html}</div>'
    fname = path_to_csv[51:58] + ".html" # use this to parse file name from path
    mpld3.save_html(fig, fname) # use this to save file locally

    return centered_html

def get_monthly_heatmap():
    all_months = {"2020_03": 0, "2020_04": 0, "2020_05": 0, "2020_06": 0, "2020_07": 0,
                  "2020_08": 0, "2020_09": 0, "2020_10": 0, "2020_11": 0, "2020_12": 0, "2021_01": 0,
                  "2021_02": 0, "2021_03": 0, "2021_04": 0, "2021_05": 0, "2021_06": 0, "2021_07": 0,
                  "2021_08": 0, "2021_09": 0, "2021_10": 0, "2021_11": 0, "2021_12": 0, "2022_01": 0,
                  "2022_02": 0, "2022_03": 0, "2022_04": 0, "2022_05": 0, "2022_06": 0, "2022_07": 0,
                  "2022_08": 0, "2022_09": 0, "2022_10": 0, "2022_11": 0, "2022_12": 0}

    count = 0
    for r, d, f in os.walk("C:/Users/Jaime/Documents/hydrated_combined_monthly/"):
        for file in f:  # iterate over every file
            full_path = os.path.join(r, file)
            all_months[file[0:7]] = get_tweet_heatmap(full_path)
            print(file[0:7])
            print(file)

    return all_months

import os
import re
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import pycountry as pycountry
import matplotlib.colors as colors
from matplotlib.colors import ListedColormap


def combine_jsonl(path):
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


if __name__ == '__main__':
    # all_dirs = os.listdir("F:/ca400/hydrated_monthly")
    # print(all_dirs)
    #
    # for i in range(len(all_dirs)):
    #     path = f'F:/ca400/hydrated_monthly/{all_dirs[i]}'
    #     combine_jsonl(path)
    # Should be 13866 lines in 2020_03

    df_path = "F:/ca400/hydrated_combined_monthly/2020_03.csv"
    basename = df_path.split("/")[-1]
    df = pd.read_csv("F:/ca400/hydrated_combined_monthly/2020_03.csv")
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

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(country_counts)

    print(list(pycountry.countries))

    # Convert country names to iso_a3 format
    for country_name in country_counts.index:
        try:
            country = pycountry.countries.get(name=country_name)
            print(country)
            if country is None:
                country = pycountry.countries.get(common_name=country_name)
                print(country)
                if country is None:
                    country = pycountry.countries.get(official_name=country_name)
                    print(country)
            iso_a3 = country.alpha_3
        except AttributeError:
            iso_a3 = 'Unknown'
        country_counts.rename(index={country_name: iso_a3}, inplace=True)

    # Print the country counts
    print(country_counts)

    # Load the world map shapefile into a geopandas GeoDataFrame
    world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge the country counts data with the world map GeoDataFrame using ISO country codes
    merged_data = world_map.merge(country_counts, how='left', left_on='iso_a3', right_index=True)

    # Fill any missing country count values with zero
    merged_data['place'].fillna(0, inplace=True)

    # Define the custom interval boundaries
    interval_bounds = [1, 10, 50, 200, 400, 1000, 2000, 7000]

    # Define the custom color map
    custom_colors = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#084594']
    custom_cmap = colors.ListedColormap(custom_colors)
    custom_norm = colors.BoundaryNorm(interval_bounds, len(custom_colors))

    # Plot the choropleth map using the merged data with custom color scaling
    fig, ax = plt.subplots(figsize=(10, 6))
    merged_data.plot(column='place', cmap=custom_cmap, norm=custom_norm, linewidth=0.8, edgecolor='0.8', ax=ax,
                     legend=True,
                     legend_kwds={'label': 'Monthly Tweet Frequency', 'orientation': 'horizontal'})
    ax.axis('off')
    ax.set_title(f'Tweet Heatmap {basename.split(".")[0]}')
    plt.show()

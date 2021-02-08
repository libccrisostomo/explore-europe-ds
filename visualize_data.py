import os
import pandas as pd
from functions import plot_sunburst
from functions import plot_scatter
from functions import join_locations

# This file returns sunburst plots for each file in the folder 'Processed .xlsx files' and saves them to 'Plots'
df_joined_locations = None  # will be used in next plot
origin_directory = '.\\Data\\Processed .xlsx files'
for filename in os.listdir(origin_directory):
    df = pd.read_excel(origin_directory + '\\' + filename, header=0, index_col=0)
    # will be used in next plot
    if df_joined_locations is None:
        df_joined_locations = pd.merge(df.drop_duplicates(), df.groupby(
            by='City').count().rename(columns={'Country': 'Number of jobs'}), on='City')
    elif filename[-7:-5] != 'EU':  # this is for my personalized sample
        df_joined_locations = join_locations(df_joined_locations, df)
    plot_sunburst(df, show=False, save='html', location=filename[filename.rfind(' ')+1:filename.rfind('.')])

# Plot with average salary, cost of living, and number of jobs per city
plot_scatter(df_joined_locations, show=False, save='hmtl')

del df, df_joined_locations, origin_directory, filename

import plotly.express as px
import os
import pandas as pd
from collect_data import plot_sunburst
from collect_data import plot_scatter
from collect_data import join_locations

# This file returns sunburst plots for each file in the folder 'Processed .xlsx files' and saves them to 'Results'
df_joined_locations = None  # will be used in next plot
origin_directory = '.\\Data\\Processed .xlsx files'
filename='job_locations_EU.xlsx'
for filename in os.listdir(origin_directory):
    df = pd.read_excel(origin_directory + '\\' + filename, header=0, index_col=0)
    # will be used in next plot
    if df_joined_locations is None:
        df_joined_locations = pd.merge(df.drop_duplicates(), df.groupby(
            by='City').count().rename(columns={'Country': 'Number of jobs'}), on='City')
    elif filename[-7:-5] != 'EU':  # this is for my personalized sample
        df_joined_locations = join_locations(df_joined_locations, df)
    plot_sunburst(df, show=False, save=None, location=filename[-7:-5])

# Plot with average salary, cost of living, and number of jobs per city
plot_scatter(df_joined_locations, show=True, save='html')

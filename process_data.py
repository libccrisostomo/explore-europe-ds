import pandas as pd
from collect_data import process_df

df_eu = pd.read_csv('job_locations_EU.txt', header=None, encoding='ISO-8859-1')
df_eu = process_df(df_eu)

df_pt = pd.read_csv('job_locations_PT.txt', header=None, encoding='ISO-8859-1')
df_pt = process_df(df_pt, 'Portugal')

df_de = pd.read_csv('job_locations_PT.txt', header=None, encoding='ISO-8859-1')
df_de = process_df(df_de, 'Portugal')

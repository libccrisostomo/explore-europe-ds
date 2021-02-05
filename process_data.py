import pandas as pd
from collect_data import process_df

df_eu = pd.read_csv('job_locations_EU.txt', header=None, encoding='ISO-8859-1')
df_eu = process_df(df_eu)

df_pt = pd.read_csv('job_locations_PT.txt', header=None, encoding='ISO-8859-1')
df_pt = process_df(df_pt, 'Portugal')

df_de = pd.read_csv('job_locations_DE.txt', header=None, encoding='ISO-8859-1')
df_de = process_df(df_de, 'Germany')

df_nl = pd.read_csv('job_locations_NL.txt', header=None, encoding='ISO-8859-1')
df_nl = process_df(df_nl, 'Netherlands')
#
# df_irl = pd.read_csv('job_locations_PT.txt', header=None, encoding='ISO-8859-1')
# # df_irl = process_df(df_irl, 'Ireland')

df_at = pd.read_csv('job_locations_AT.txt', header=None, encoding='ISO-8859-1')
df_at = process_df(df_at, 'Austria')
#
# df_it = pd.read_csv('job_locations_PT.txt', header=None, encoding='ISO-8859-1')
# df_it = process_df(df_it, 'Italy')
#
# df_dk = pd.read_csv('job_locations_PT.txt', header=None, encoding='ISO-8859-1')
# df_dk = process_df(df_dk, 'Denmark')
#
# df_fr = pd.read_csv('job_locations_PT.txt', header=None, encoding='ISO-8859-1')
# df_fr = process_df(df_dk, 'France')

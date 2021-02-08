import pandas as pd
from functions import process_df
import os

# This file transforms the files from the folder 'Raw .txt files' into processed Excel files, which will be saved
# to the folder 'Processed .xlsx files'

origin_directory = '.\\Data\\Raw .txt files'
filename = 'job_locations_EU.txt'
for filename in os.listdir(origin_directory):
    df = pd.read_csv(origin_directory + '\\' + filename, header=None, encoding='ISO-8859-1')
    df = process_df(df, country_filter=True)
    df.to_excel('.\\Data\\Processed .xlsx files\\' + filename[:filename.rfind('.')] + '.xlsx')
    print('Processed the file ' + filename + ' and saved as ' + filename[:filename.rfind('.')] + '.xlsx')

del filename, origin_directory, df


import pandas as pd
from sklearn.impute import KNNImputer
from sklearn import preprocessing
import numpy as np

# importing job location data
df = pd.read_csv('job_locations.txt', header=None, encoding='ISO-8859-1')
df.columns = ['City', 'Region', 'Country']

# Processing data

# Missing values in Country
# if a record only has a missing value in country, we can assume that the country name is in the 'Region' column
df.Country = df.Country.fillna(df['Region'])

# Dropping Region: Region is not really interesting... column can be dropped
df.drop(['Region'], axis=1, inplace=True)

# Dropping Remote jobs 
# If the City name is = 'remote', then there is no location for the job
df = df.loc[df.City != 'Remote']

# eliminte the words 'Metropolian' and 'Area' from city names
df['City'].str.split(' ', expand=True)
df['City'] = df['City'].map(lambda x: x.replace('Metropolitan', '').replace(
    'Area', '').replace('Region', '').replace('Community of', '').replace(
    'Greater', '').strip())

# Remaining missing values in Country
# some of these missing values can be imputed. For instance, if a record with 'City'='Paris', we can deduce from the
# remaining data that the missing country is 'France'
imputer = KNNImputer(n_neighbors=10)
# converting missing values to strings
df[pd.isnull(df)] = 'NaN'
# saving indices of NaN
df_nan_index = df.loc[df.Country == 'NaN'].index

# encoding cities and countries, to apply the KKN Imputer
# defining and fitting label encoder instances for City and Country
le_city = preprocessing.LabelEncoder()
le_country = preprocessing.LabelEncoder()

df['City'] = le_city.fit_transform(df['City'])
df['Country'] = le_country.fit_transform(df['Country'])

# reinserting missing values
df.loc[df.index.isin(df_nan_index), 'Country'] = np.nan

# filling missing values
df = pd.DataFrame(imputer.fit_transform(df), columns=['City', 'Country'])
# KNN Imputer returns the average value of the nearest neighbors, but we want int only
df = df.astype('int32')

# transforming the labels back to city and country names
df['City'] = le_city.inverse_transform(df['City'])
df['Country'] = le_country.inverse_transform(df['Country'])

# manually checking of every imputation is right...
check_df = df.loc[df.index.isin(df_nan_index)]  # seems so!

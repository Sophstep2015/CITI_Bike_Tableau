import pandas as pd

#import os
df = pd.read_csv('2020new.csv')
df.head()
df.shape
#Check for Null Values
df.isnull().sum()
#Reorder Columns
df2 = df[['started_at', 'ended_at', 'start_station_name','start_station_id','end_station_name','end_station_id','start_lat','start_lng', 'end_lat', 'end_lng', 'usertype', 'birth year', 'gender']]
#Convert Gender Column 
df2['gender'] = df2['gender'].str.replace('1', 'Male')
df2['gender'] = df2['gender'].str.replace('2', 'Female')
df2['gender'] = df2['gender'].str.replace('0', 'Female')
#Export Clean Data to CSV
df2.to_csv(('clean_2020_demo1.csv'), index = False)
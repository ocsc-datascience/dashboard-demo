#!/usr/bin/env python3
import sys
import csv
import pandas as pd

df = pd.read_csv('../assets/raw/weather_cities.csv')
df.index.name = 'City_ID'
df['Date'] = "2018-07-23"

df.rename(columns={ 'city':'City',
                    'lon':'Lon',
                    'lat':'Lat',
                    'temperature':'Max. Temp',
                    'cloudiness':'Cloudiness',
                    'humidity':'Humidity',
                    'wind speed':'Wind Speed'},
          inplace=True)

df['City'] = df['City'].str.title()

outstring = df.to_html()

with open("table-raw.html","w") as outfile:
    outfile.write(outstring)
    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = pd.read_csv('C:/Users/Matti/.spyder-py3/UFOdata.csv')
Statedata = pd.read_csv('C:/Users/Matti/.spyder-py3/USStatePopulations.csv')

data.dropna().describe()
print(data.isnull().sum())
print("\n")

"Måsta ta bort time från datetime då det skapade problem pga fel formaterat"
data['oldTime'] = data['datetime']
data['datetime'] = data['datetime'].str.split(expand=True)[0]
data['datetime'] = pd.to_datetime(data['datetime'])
data['year'] = data['datetime'].dt.year
data['month'] = data['datetime'].dt.month

"Dela upp kolumner i egna tabeller"
month = data['month'].value_counts()
year = data['year'].value_counts()
countries = data['country'].value_counts()
states = data['state'].value_counts()
cities = data['city'].value_counts()
shape = data['shape'].value_counts()
duration = data['duration (seconds)'].value_counts()
germany = data[(data.country == "de")]

"Skapa en säsong tabell"
def season_calc(x):
    x = int(x.split("/")[0])
    if x in range(3,6):
        return "Spring"
    if x in range(6,9):
        return "Summer"
    if x in range(9,12):
        return "Autumn"
    if x == 1 or x == 2 or x == 12:
        return "Winter"

data["Season"] = data['oldTime'].apply(season_calc)

print('Unique countries: ', len(data['country'].unique()))
print('Unique states: ', len(data['state'].unique()))
print('Unique shapes: ', len(data['shape'].unique()))


data['duration(seconds)_num']=data['duration (seconds)'].astype(float)
sightTime = round(data['duration (seconds)'].mean())
print('Average sight time: {0} seconds'.format(sightTime))
medianTime = round(data['duration (seconds)'].median(), 2)
print('Median sighting time: {0} seconds'.format(medianTime))

"Icke fungerande"
"plt.figure(figsize=(35,5))"
"medianTime2 = data.groupby('year').agg('mean').reset_index()"
"plt.bar(medianTime2['year'], medianTime2['duration (seconds)'])"
"plt.suptitle('Average sights per year', fontsize=35)"

data.head(10)

"Sikter per säsong"
data['Season'].value_counts().plot(kind='bar')
plt.title("Sights per season")
plt.show()

"Sikter per land"
x_pos = range(len(countries))
plt.bar(x_pos, countries, align="center", alpha=0.5)
plt.xlabel('Countries');
plt.ylabel('Sights');

"Stat diagram, måste köras separat då det skapar ett dubbel diagram annars"
"labels = 'California', 'Washington', 'Florida', 'Texas','New York', 'Arizona', 'Illinois', 'Pennsylvania','Ohio','Michigan'"
"plt.pie(states.head(10), labels=labels)"


"Sikter per år diagram"
plt.figure(figsize=(10,5))
plt.title("UFO sightings by year")
plt.xlabel("Years")
plt.ylabel("number of sighting")
data.datetime.dt.year.value_counts().plot(kind = "line");
data.datetime.value_counts().plot(kind='line')

"Sights per månad"
plt.bar(data['month'], align="center", alpha=0.5, height=2)
plt.xlabel('month');
plt.ylabel('Sights');
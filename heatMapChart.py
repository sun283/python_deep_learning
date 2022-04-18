# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rc('font', family='NanumBarunGothic')
# Load a file under "data" folder
file = "/gdrive/My Drive/data/data_2021.csv"
data = pd.read_csv(file)

# 집계일자
data_06_22 = data[data.집계시.isin(range(6,23))]
# Create data_06_22 Dataframe with counting by 집계시
data_06_22.sort_values(by='집계시')
data_06_22_day = data_06_22.groupby('집계일자')['도착영업소코드'].value_counts()
data_06_22_day = data_06_22.groupby('집계일자')['도착영업소코드'].value_counts().unstack()
data_06_22_day = data_06_22.groupby('집계일자')['도착영업소코드'].value_counts().unstack(level=0)
data_06_22_day = data_06_22.groupby('집계일자')['도착영업소코드'].value_counts().unstack().fillna(0)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(20,30))
sns.heatmap(data_06_22_day, annot=True, fmt=".0f", linewidths=.5, ax=ax, cmap="YlGnBu" )

# 집계시
data_06_22_time = data_06_22.groupby('집계시')['도착영업소코드'].value_counts().unstack().fillna(0)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(20,30))
sns.heatmap(data_06_22_time, annot=True, fmt="d", linewidths=.5, ax=ax) 

# 요일별
data_06_22_weekdays = data_06_22.groupby('요일')['도착영업소코드'].value_counts().unstack().fillna(0)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(20,30))
sns.heatmap(data_06_22_weekdays, annot=True, fmt="d", linewidths=.5, ax=ax, cmap="YlGnBu" )


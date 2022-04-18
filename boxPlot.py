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

# Histogram
plt.figure(figsize=(20,10))
sns.histplot(data[data['도착영업소코드'] == 110]['통행시간'], color='green', label='목천')
sns.histplot(data[data['도착영업소코드'] == 125]['통행시간'], color='blue', label='남구미')
sns.histplot(data[data['도착영업소코드'] == 140]['통행시간'], color='red', label='부산')
# label을 보여주기 위함
plt.legend(title='도착영업소')
plt.show()

# Box Plot
# Configure figure size
plt.figure(figsize=(20,10))
sns.set(style="ticks", palette="pastel")
# Draw a nested boxplot to show Pace by Gender
sns.boxplot(x="도착영업소코드", y="통행시간", data=data)
plt.show()

data_statistics = data[data['도착영업소코드'] == 130]['통행시간'].describe()
data_statistics = data[data['도착영업소코드'] == 140]['통행시간'].describe()

# Configure figure size
plt.figure(figsize=(20,10))
sns.set(style="ticks", palette="pastel")
# Draw a nested boxplot to show Pace by Gender
sns.boxplot(x="요일", y="통행시간", data=data)
plt.show()

# Configure figure size
plt.figure(figsize=(20,10))
sns.set(style="ticks", palette="pastel")
# Draw a nested boxplot to show Pace by Gender
sns.boxplot(x="집계시", y="통행시간", data=data)
plt.show()

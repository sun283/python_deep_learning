# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()
plt.rc('font', family='NanumBarunGothic')
# Load a file under "data" folder
file = "/gdrive/My Drive/data/data_2021.csv"
data = pd.read_csv(file)

# Histoplot
# Configure figure size
plt.figure(figsize=(20,10))
# Create histogram - Distribution Rate
data_destination = sns.histplot(data=data, x='도착영업소코드')
data_destination.set_xlabel('도착영업소코드',fontdict= {'size':16})
data_destination.set_ylabel('Distribution Rate',fontdict= {'size':16})
data_destination.set_title('Distribution Rate by 도착영업소코드',fontsize=18)
plt.show()

# Count plot
# Configure figure size
plt.figure(figsize=(20,10))
# Create histogram - Distribution Rate
data_destination = sns.countplot(data=data, x='도착영업소코드')
data_destination.set_xlabel('도착영업소코드',fontdict= {'size':16})
data_destination.set_ylabel('통행회수',fontdict= {'size':16})
data_destination.set_title('통행회수 by 도착영업소코드',fontsize=18)
plt.show()

# Configure figure size
plt.figure(figsize=(20,10))
# Create histogram - Distribution Rate
data_destination = sns.countplot(data=data, x='도착영업소코드', order=data['도착영업소코드'].value_counts().index)
data_destination.set_xlabel('도착영업소코드',fontdict= {'size':16})
data_destination.set_ylabel('통행회수',fontdict= {'size':16})
data_destination.set_title('통행회수 by 도착영업소코드',fontsize=18)
plt.show()

# Histogram
plt.figure(figsize=(20,10))
sns.histplot(data[data['도착영업소코드'] == 110]['통행시간'], color='green', label='목천')
sns.histplot(data[data['도착영업소코드'] == 125]['통행시간'], color='blue', label='남구미')
sns.histplot(data[data['도착영업소코드'] == 140]['통행시간'], color='red', label='부산')
# label을 보여주기 위함
plt.legend(title='도착영업소')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=data, x='통행시간', hue='도착영업소코드')
plt.show()


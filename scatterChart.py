# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='NanumBarunGothic')
# Load a file under "data" folder
file = "/gdrive/My Drive/data/data_2021.csv"
data = pd.read_csv(file)

# 집계시
data_06_22 = data[data.집계시.isin(range(6,23))]
# Create data_06_22 Dataframe with counting by 집계시
data_06_22.sort_values(by='집계시')
# Store index of data_06_22_counting into x
data_06_22_counting = data_06_22['집계시'].value_counts()
data_06_22_counting_sorted = data_06_22_counting.sort_index()

# Create Scatter Plot Chart
plt.scatter(data_06_22_counting_sorted.index, data_06_22_counting_sorted.values)

data_06_22_time = data_06_22['통행시간']
# Configure figure size
plt.figure(figsize=(20,10))
# Create Scatter Plot Chart
plt.scatter(data_06_22_time.index, data_06_22_time .values, c="g", alpha=0.5)
# Generate title
plt.title('순번 기준 통행회수', fontsize=18)
plt.xlabel('순번', fontdict={'size':16})
plt.ylabel('통행회수', fontdict={'size':16})
# Show plot
plt.show()

# 집계일자 기준
data_days = data.groupby(by=['집계일자']).mean()
data_days_time = data_days['통행시간']
x = data_days_time.index
labels = [str(i) for i in x]
# Store values of data_days_time into values
values = data_days_time.values

# Configure figure size
plt.figure(figsize=(20,10))
# Create Scatter Plot Chart
plt.scatter(labels, values, c="g", alpha=0.5)
# Generate title
plt.title('집계일 기준 통행시간', fontsize=18)
plt.xlabel('집계일', fontdict={'size':16})
plt.ylabel('통행시간', fontdict={'size':16})
# Show plot
plt.show()

# Configure figure size
plt.figure(figsize=(20,10))
# Create Scatter Plot Chart
plt.scatter(values, labels, c="g", alpha=0.5)
# Generate title
plt.title('집계일 기준 통행회수', fontsize=18)
plt.xlabel('통행시간', fontdict={'size':16})
plt.ylabel('집계일', fontdict={'size':16})
# Show plot
plt.show()

# 도착영업소코드
data_110_days = data[data['도착영업소코드'] == 110].groupby(by=['집계일자']).mean()
data_125_days = data[data['도착영업소코드'] == 125].groupby(by=['집계일자']).mean()
data_140_days = data[data['도착영업소코드'] == 140].groupby(by=['집계일자']).mean()

data_110_days_time = data_110_days['통행시간']
data_125_days_time = data_125_days['통행시간']
data_140_days_time = data_140_days['통행시간']

# Configure figure size
plt.figure(figsize=(20,10))
# Create Scatter Plot Chart
plt.scatter(data_110_days_time.values, labels, c="g", alpha=0.5)
plt.scatter(data_125_days_time.values, labels, c="b", alpha=0.5)
plt.scatter(data_140_days_time.values, labels, c="r", alpha=0.5)
# Generate title
plt.title('도착영업소 기준 통행시간', fontsize=18)
plt.xlabel('통행시간', fontdict={'size':16})
plt.ylabel('도착영업소', fontdict={'size':16})
# Show plot
plt.show()
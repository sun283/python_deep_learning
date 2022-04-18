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

# Store index of data_06_22_counting into x
x = data_06_22_counting_sorted.index
labels = [str(i) + '시' for i in x]
# Store values of data_06_22_counting into values
values = data_06_22_counting_sorted.values

# Configure figure size
plt.figure(figsize=(20,10))
# Create Bubble Chart
plt.scatter(labels, values, s=values, c="b", alpha=0.5)
# Generate title
plt.title('집계시 기준 통행회수', fontsize=18)
plt.xlabel('집계시', fontdict={'size':16})
plt.ylabel('통행회수', fontdict={'size':16})
# Show plot
plt.show()

# 도착영업소코드
data_destination_counting = data['도착영업소코드'].value_counts()
data_destination_counting_sorted = data_destination_counting.sort_index()
x = data_destination_counting_sorted.index
labels = [str(i) for i in x]
labels = ['기흥', '목천', '대전', '부산', '남구미', '경주', '동김천', '황간']
# Store values of data_destination_counting_sorted into values
values = data_destination_counting_sorted.values
# Configure figure size
plt.figure(figsize=(20,10))
# Create Bubble Chart
plt.scatter(labels, values, s=values, c="b", alpha=0.5)
# Generate title
plt.title('도착영업소 기준 통행회수', fontsize=18)
plt.xlabel('도착영업소', fontdict={'size':16})
plt.ylabel('통행회수', fontdict={'size':16})
# Show plot
plt.show()

# 요일별
data_weekdays_mean = data.groupby(by=['요일']).mean()
data_weekdays_count = data.groupby(by=['요일']).count()

data_weekdays_mean_time = data_weekdays_mean['통행시간']
data_weekdays_count_time = data_weekdays_count['통행시간']

# Store index of data_weekdays_mean_time into x
x = data_weekdays_mean_time.index
labels = ['월', '화', '수', '목', '금', '토', '일']
# Store values of data_weekdays_mean_time into values
values = data_weekdays_mean_time.values
counts = data_weekdays_count_time.values
colors = np.random.rand(len(labels))

# Configure figure size
plt.figure(figsize=(20,10))
# Create Bubble Chart
plt.scatter(labels, values, s=counts, c=colors, alpha=0.5)
# Generate title
plt.title('요일 기준 통행시간', fontsize=18)
plt.xlabel('요일', fontdict={'size':16})
plt.ylabel('통행시간', fontdict={'size':16})
# Show plot
plt.show()
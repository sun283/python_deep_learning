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

# Create Line Chart
plt.plot(data_06_22_counting_sorted.index, data_06_22_counting_sorted.values)

# Store index of data_06_22_counting into x
x = data_06_22_counting_sorted.index
labels = [str(i) + '시' for i in x]
# Store values of data_06_22_counting_ sorted into values
values = data_06_22_counting_sorted.values

# Configure figure size
plt.figure(figsize=(20,10))
# Create Line Chart
plt.plot(labels, values, marker='s', color='r')
# Generate title
plt.title('집계시 기준 통행회수', fontsize=18)
plt.xlabel('집계시', fontdict={'size':16})
plt.ylabel('통행회수', fontdict={'size':16})
# Show plot
plt.show()

# 도착영업소코드
data_destination_counting = data['도착영업소코드'].value_counts()
data_destination_counting_sorted = data_destination_counting.sort_index()
# Store index of data_06_22_destination_counting_sorted into x
x = data_destination_counting_sorted.index
# Convert x values to String in order to avoid int sorting
labels = [str(i) for i in x]
# 101 서울, 105 기흥, 110 목천, 115 대전, 120 황간, 125 남구미, 130 동김천, 135 경주, 140 부산
labels = ['기흥', '목천', '대전', '황간', '남구미', '동김천', '경주', '부산']
# Store values of data_destination_counting_sorted into values
values = data_destination_counting_sorted.values

# Configure figure size
plt.figure(figsize=(20,10))
# Create Pie Chart
plt.plot(labels, values, marker='*', color='b')
# Generate title
plt.title('집계시 기준 통행회수', fontsize=18)
plt.xlabel('집계시', fontdict={'size':16})
plt.ylabel('통행회수', fontdict={'size':16})
# Show plot
plt.show()

# 요일별
data_weekdays = data.groupby(by=['요일']).mean()
data_weekdays_time = data_weekdays['통행시간']
# Store index of data_weekdays_time into x
x = data_weekdays_time.index
labels = ['월', '화', '수', '목', '금', '토', '일']
values = data_weekdays_time.values

# Configure figure size
plt.figure(figsize=(20,10))
# Create Line Chart
plt.plot(labels, values, marker='d', color='g')
# Generate title
plt.title('요일 기준 통행시간', fontsize=18)
plt.xlabel('요일', fontdict={'size':16})
plt.ylabel('통행시간', fontdict={'size':16})
# Show plot
plt.show()
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
# Store index of data_06_22_counting into x
x = data_06_22_counting.index
# Convert x values to String in order to avoid int sorting
labels = [str(i) + '시' for i in x] 
explode = [0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Store values of data_06_22_counting into values
values = data_06_22_counting.values

# Configure figure size
plt.figure(figsize=(7,7))
# Create Pie Chart
plt.pie(values, explode=explode, labels=labels, startangle=90, shadow=True, autopct='%.1f')
# Generate title
plt.title('집계시 기준 통행회수', fontsize=18)
# Show plot
plt.show()

# 도착영업소코드
data_destination_counting = data['도착영업소코드'].value_counts()
# Store index of data_06_22_counting into x
x = data_destination_counting.index
# Convert x values to String in order to avoid int sorting
labels = [str(i) for i in x] 
# 101 서울, 105 기흥, 110 목천, 115 대전, 120 황간, 125 남구미, 130 동김천, 135 경주, 140 부산
labels = ['기흥', '목천', '대전', '부산', '남구미', '경주', '동김천', '황간']
explode = [0.2, 0.1, 0, 0, 0, 0, 0, 0]
# Store values of data_destination_counting into values
values = data_destination_counting.values

# Configure figure size
plt.figure(figsize=(7,7))
# Create Pie Chart
plt.pie(values, explode=explode, labels=labels, startangle=90, shadow=True, autopct='%.1f%%', counterclock=False)
# Generate title
plt.title('도착영업소코드 기준 통행회수', fontsize=18)
# Show plot
plt.show()


# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='NanumBarunGothic')
file = "/gdrive/My Drive/data/data_2021.csv"
data = pd.read_csv(file)

# 집계시별 데이터
data_06_22 = data[data.집계시.isin(range(6,23))]
data_06_22.sort_values(by='집계시')

# Store index of data_06_22_counting into x
data_06_22_counting = data_06_22['집계시'].value_counts()
# Store index of data_06_22_counting into x
x = data_06_22_counting.index
# Convert x values to String in order to avoid int sorting
x = [str(i) for i in x] 
# Store values of data_06_22_counting into y
y = data_06_22_counting.values
# Calculate ratio and accumulated ratio
ratio = y / y.sum()
ratio_sum = ratio.cumsum()

# Configure figure size
fig, barChart = plt.subplots(figsize=(20,10))
# Create Bar Chart
barChart.bar(x, y)
# Create Line Chart
lineChart = barChart.twinx()
lineChart.plot(x, ratio_sum, '-ro', alpha=0.5)
# Create right side labels
ranges = lineChart.get_yticks()
print(ranges)
lineChart.set_yticklabels(['{:,.1%}'.format(x) for x in ranges])
# Create annotations on Line Chart
ratio_sum_percentages = ['{0:.0%}'.format(x) for x in ratio_sum]
for i, txt in enumerate(ratio_sum_percentages):
  lineChart.annotate(txt, (x[i], ratio_sum[i]), fontsize=14)
# Generate labels and title
barChart.set_xlabel('집계시', fontdict={'size':16})
barChart.set_ylabel('통행회수', fontdict={'size':16})
plt.title('Pareto Chart - 통행회수 by 집계시', fontsize=18)
# Show plot
plt.show()

# 도착 영업소 관점에서 보는 Pareto Chart
data_destination_counting = data['도착영업소코드'].value_counts()
# Store index of data_06_22_counting into x
x = data_destination_counting.index
# Convert x values to String in order to avoid int sorting
x = [str(i) for i in x] 
# Store values of data_06_22_counting into y
y = data_destination_counting.values
# Calculate ratio and accumulated ratio
ratio = y / y.sum()
ratio_sum = ratio.cumsum()

# Configure figure size
fig, barChart = plt.subplots(figsize=(20,10))
# Create Bar Chart
barChart.bar(x, y)
# Create Line Chart
lineChart = barChart.twinx()
lineChart.plot(x, ratio_sum, '-ro', alpha=0.5)
# Create right side labels
ranges = lineChart.get_yticks()
print(ranges)
lineChart.set_yticklabels(['{:,.1%}'.format(x) for x in ranges])
# Create annotations on Line Chart
ratio_sum_percentages = ['{0:.0%}'.format(x) for x in ratio_sum]
for i, txt in enumerate(ratio_sum_percentages):
  lineChart.annotate(txt, (x[i], ratio_sum[i]), fontsize=14)
# Generate labels and title
barChart.set_xlabel('집계시', fontdict={'size':16})
barChart.set_ylabel('통행회수', fontdict={'size':16})
plt.title('Pareto Chart - 통행회수 by 도착영업소코드', fontsize=18)
# Show plot
plt.show()
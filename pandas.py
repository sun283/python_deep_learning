# This code is working on google colab
# needs to be altered using pydrive
# Mount Drive
# from google.colab import drive
# drive.mount('/gdrive')

# Load Data
import pandas as pd
# Load a file under "data" folder
file = "/gdrive/My Drive/data/TCS_영업소간통행시간_1시간_1개월_202101.csv"
data = pd.read_csv(file, sep=",", encoding="euc-kr")

# 상위 5줄만 출력
print(data.head())
# 상위 10줄 출력
print(data.head(10))
# 하위 5줄만 출력
print(data.tail())
# 파일 정보 출력
print(data.info())

# Clean Data
# Checking the null value in the data fields
data.isnull().sum(axis=0)

# Show columns of the data frame
data.columns

# Drop some columns with null values
data_clean = data.drop(['Unnamed: 6'], axis='columns')

data_clean.head()

# data_clean['통행시간']도 가능하다.
data_clean.통행시간 > 0
(data_clean.통행시간 > 0).unique()
data_clean = data_clean[data_clean.통행시간 > 0]
data_clean.head()
data_clean.info()

# Read columns
# select by '.' Operator
data.집계일자

# select Only by '[]' Operator
data["Unnamed: 6"]
# select by '[]' Operator
data["집계일자"]

# Select Data
data_clean.head()

# 특정 번호의 행을 가져오는 방법
data_clean[0:5]

# 필요한 컬럼만 가져오는 방법
df_data = pd.DataFrame(data_clean, columns=["집계일자", "집계시", "출발영업소코드", "도착영업소코드", "통행시간"])
print(df_data)

#특정 조건의 데이터만 가져오는 방법
long_distance = df_data.통행시간 > 700
print(long_distance)

start_from_101 = df_data[df_data.출발영업소코드 == 101]
print(start_from_101)

# 101: 서울, 105: 기흥, 110: 목천, 115: 대전, 120: 황간, 125: 남구미, 130: 동김천, 135: 경주, 140: 부산
start_from_101_to_140 = start_from_101[start_from_101['도착영업소코드'].isin([105,110,115,120,125,130,135,140])]
print(start_from_101_to_140)

print(start_from_101_to_140.head())

# Convert & Insert Data
# 요일정보
# The days are numbered from 0 to 6 where 0 is Monday and 6 is Sunday.
# 3 Ways of Adding new columns to Pandas Dataframe
# https://re-thought.com/how-to-add-new-columns-in-a-dataframe-in-pandas/
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

# 1: By declaring a new list as a column
start_from_101_to_140['요일'] = pd.to_datetime(start_from_101_to_140['집계일자'], format='%Y%m%d').dt.dayofweek
print(start_from_101_to_140.head())

# 2: Using.loc[]
start_from_101_to_140.loc[:, '요일'] = pd.to_datetime(start_from_101_to_140['집계일자'], format='%Y%m%d').dt.dayofweek
print(start_from_101_to_140.head())

# 3: Using the .assign() function
start_from_101_to_140 = start_from_101_to_140.assign(요일=pd.to_datetime(start_from_101_to_140['집계일자'], format='%Y%m%d').dt.dayofweek)
print(start_from_101_to_140.head())

print(start_from_101_to_140.dtypes)

# Sort & Group Data
start_from_101_to_140.sort_values(by=['통행시간'])
start_from_101_to_140.sort_values(by=['통행시간'], ascending=False)
start_from_101_to_140.sort_values(by=['집계일자', '집계시'])
start_from_101_to_140.sort_values(by=['집계일자', '집계시'], ascending=False)
start_from_101_to_140.groupby(start_from_101_to_140['도착영업소코드']).mean()
start_from_101_to_140['통행시간'].groupby(start_from_101_to_140['도착영업소코드']).mean()
groupby_destination = start_from_101_to_140['통행시간'].groupby(start_from_101_to_140['도착영업소코드'])
print(groupby_destination.size())
print(groupby_destination.sum())
print(groupby_destination.mean())
print(groupby_destination.max())
print(groupby_destination.min())

# Save Data
output = "/gdrive/My Drive/data/data_202101.csv"
start_from_101_to_140.to_csv(output, index=None, header=True)

# TCS_영업소간통행시간_1시간_1개월_202102.csv
file = "/gdrive/My Drive/data/TCS_영업소간통행시간_1시간_1개월_202102.csv"
data = pd.read_csv(file, sep=",", encoding="euc-kr")

data_clean = data_clean[data_clean.통행시간 > 0]

# Drop some columns with null values
data_clean = data.drop(['Unnamed: 6'], axis='columns')

# 필요한 컬럼만 가져오는 방법
df_data = pd.DataFrame(data_clean, columns=["집계일자", "집계시", "출발영업소코드", "도착영업소코드", "통행시간"])

start_from_101 = df_data[df_data.출발영업소코드 == 101]

# 101: 서울, 105: 기흥, 110: 목천, 115: 대전, 120: 황간, 125: 남구미, 130: 동김천, 135: 경주, 140: 부산
start_from_101_to_140 = start_from_101[start_from_101['도착영업소코드'].isin([105,110,115,120,125,130,135,140])]

# Using the .assign() function
start_from_101_to_140 = start_from_101_to_140.assign(요일=pd.to_datetime(start_from_101_to_140['집계일자'], format='%Y%m%d').dt.dayofweek)
print(start_from_101_to_140)

output = "/gdrive/My Drive/data/data_202102.csv"
start_from_101_to_140.to_csv(output, index=None, header=True)

file = "/gdrive/My Drive/data/TCS_영업소간통행시간_1시간_1개월_202103.csv"
data = pd.read_csv(file, sep=",", encoding="euc-kr")
data_clean = data_clean[data_clean.통행시간 > 0]
data_clean = data.drop(['Unnamed: 6'], axis='columns')
df_data = pd.DataFrame(data_clean, columns=["집계일자", "집계시", "출발영업소코드", "도착영업소코드", "통행시간"])
start_from_101 = df_data[df_data.출발영업소코드 == 101]
start_from_101_to_140 = start_from_101[start_from_101['도착영업소코드'].isin([105,110,115,120,125,130,135,140])]
start_from_101_to_140 = start_from_101_to_140.assign(요일=pd.to_datetime(start_from_101_to_140['집계일자'], format='%Y%m%d').dt.dayofweek)
output = "/gdrive/My Drive/data/data_202103.csv"
start_from_101_to_140.to_csv(output, index=None, header=True)

# Merge
data_202101 = pd.read_csv("/gdrive/My Drive/data/data_202101.csv")
print(data_202101.head())
data_202102 = pd.read_csv("/gdrive/My Drive/data/data_202102.csv")
data_202103 = pd.read_csv("/gdrive/My Drive/data/data_202103.csv")

data_2021 = pd.concat([data_202101,data_202102,data_202103], ignore_index=True, sort=False)
print(data_2021.head())

# 특정 컬럼을 index 대신 표시한다
data_2021_by_time = pd.concat([data_202101,data_202102,data_202103], ignore_index=True, sort=False).set_index('통행시간')
print(data_2021_by_time)

final = "/gdrive/My Drive/data/data_2021.csv"
data_2021.to_csv(final, index=None, header=True)

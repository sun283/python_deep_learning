# Import libraries
from time import sleep
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from treelib import Node, Tree
import pandas as pd

## Google OAuth
gauth = GoogleAuth()
# gauth.LocalWebserverAuth() will fire up the browser and ask for your authentication. 
# Choose the google account you want to access and authorize the app.
gauth.LocalWebserverAuth()
# gauth.CommandLineAuth()
# drive = GoogleDrive(gauth) create a Google Drive object to handle file. 
# You will be using this object to list and create file.
drive = GoogleDrive(gauth)

## Constants
FOLDER_ID = 'google drive folder id'
INPUT_PREFIX = 'C:\\Users\\MSI\\data\\TCS_영업소간통행시간_1시간_1개월_2021'
OUTPUT_PREFIX = 'C:\\Users\\MSI\\data_2021'
OUTPUT_EXTENSION = '.csv'

## Variable
output_dataframes = []
# FILES = (
#     ('data_2021.csv'),
# )
FILES = []

## Function
# Retreive data from Jan. to Dec.
def generateData(month):
    month_string = str(month)
    length_month_string = len(month_string)
    if length_month_string == 1:
        month_string = '0' + month_string
    input_file = INPUT_PREFIX + month_string + OUTPUT_EXTENSION
    output_file = OUTPUT_PREFIX + month_string + OUTPUT_EXTENSION
    print('INPUT : ' + input_file, '  OUTPUT : ' + output_file)
    data = pd.read_csv(input_file, sep=",", encoding="euc-kr")
    # 결측치, 오류치를 제외
    data = data.drop(['Unnamed: 6'], axis='columns')
    data = data[data.통행시간 > 0]
    # Select : 필요한 컬럼만 선택
    # 101: 서울, 105: 기흥, 110: 목천, 115: 대전, 120: 황간, 125: 남구미, 130: 동김천, 135: 경주, 140: 부산
    data = pd.DataFrame(data, columns=["집계일자", "집계시", "출발영업소코드", "도착영업소코드", "통행시간"])
    data = data[data.출발영업소코드 == 101]
    data = data[data['도착영업소코드'].isin([105,110,115,120,125,130,135,140])]
    # Convert : 집계일자를 요일로 변환하여 삽입
    data = data.assign(요일=pd.to_datetime(data['집계일자'], format='%Y%m%d').dt.dayofweek)
    # Sort
    data.sort_values(by=['집계일자', '집계시'])
    # Save per month
    data.to_csv(output_file, index=None, header=True, encoding='euc-kr')
    output_dataframes.append(data)

# Save into Google Drive
def uploadData():
    for file_title in FILES :
        file = drive.CreateFile({'title': file_title, "mimeType": "text/csv", "parents": [{"id": FOLDER_ID}]})
        # file.SetContentFile("file.csv") will open the specified file name and set the content of the file to the GoogleDriveFile object. 
        file.SetContentFile(file_title)
        # file.Upload() to complete the upload process.
        file.Upload()
        print('Created file %s with mimeType %s' % (file['title'], file['mimeType']))

## Upload file in Google Drive(Single File)
# file = drive.CreateFile({'title': 'file.csv', "parents": [{"id": FOLDER_ID}]})
# file.SetContentString('TEST')
# file.Upload()

def main():
    global FILES
    for month in range(1,13):
        generateData(month)
    output_data = pd.concat(output_dataframes, ignore_index=True, sort=False)
    final = OUTPUT_PREFIX + OUTPUT_EXTENSION
    output_data.to_csv(final, index=None, header=True, encoding='euc-kr')
    str_split = OUTPUT_PREFIX.split('\\')
    FILES.append(str_split[3] + OUTPUT_EXTENSION)
    FILES = tuple(FILES)
    uploadData()
    ## Refs functions
    # sleep(10)
    # file.Trash()  # Move file to trash.
    # file.UnTrash()  # Move file out of trash.
    # file.Delete()  # Permanently delete the file.

if __name__ == "__main__":
    main()

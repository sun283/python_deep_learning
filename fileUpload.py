# Import libraries
from time import sleep
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

## Google OAuth
gauth = GoogleAuth()
gauth.CommandLineAuth()
# gauth.LocalWebserverAuth() will fire up the browser and ask for your authentication. Choose the google account you want to access and authorize the app.
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth) create a Google Drive object to handle file. You will be using this object to list and create file.
drive = GoogleDrive(gauth)

fileList = drive.ListFile({'q': "'<folder ID>' in parents and trashed=false"}).GetList()
print(fileList)

# Constant
# FOLDER_ID = 'google drive folder id'
FOLDER_ID = '1Yl-gXUlJY02ZNkOf0ItiOwf0y0ud-VPC'
FILES = (
    ('data_2021.csv'),
)

## Upload file in Google Drive
# file = drive.CreateFile({'title': 'file.csv', "parents": [{"id": FOLDER_ID}]})
# file.SetContentString('TEST')
# file.Upload()

for file_title in FILES :
    file = drive.CreateFile({'title': file_title, "parents": [{"id": FOLDER_ID}]})
    # file.SetContentFile("file.csv") will open the specified file name and set the content of the file to the GoogleDriveFile object. 
    file.SetContentFile('file.csv')
    # file.Upload() to complete the upload process.
    file.Upload()
    print('Created file %s with mimeType %s' % (file['title'], file['mimeType']))
    sleep(10)
    # file.Trash()  # Move file to trash.
    # file.UnTrash()  # Move file out of trash.
    file.Delete()  # Permanently delete the file.

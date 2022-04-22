# Import libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

 # Google OAuth
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

# Constant
FOLDER_ID = 'Google Drive Folder ID'

# Upload file to Google Drive
file = drive.CreateFile({'title': 'file.csv', "parents": [{"id": FOLDER_ID}]})
file.SetContentString('TEST')
file.Upload()
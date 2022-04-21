# Import Libraries
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Google Drive oauth2
try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET_FILE = r'C:\\lgy\\python\\store.json'
CREDENTIAL_FILENAME = 'drive_python_upload.json'

store = file.Storage(CREDENTIAL_FILENAME)
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    ('file.csv'),
)

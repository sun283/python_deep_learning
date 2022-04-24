# Import libraries
from time import sleep
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from treelib import Node, Tree

# switch current directory into the directory where the script exists
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

## Google OAuth
gauth = GoogleAuth()
# gauth.LocalWebserverAuth() will fire up the browser and ask for your authentication. Choose the google account you want to access and authorize the app.
gauth.LocalWebserverAuth()
# gauth.CommandLineAuth()
# drive = GoogleDrive(gauth) create a Google Drive object to handle file. You will be using this object to list and create file.
drive = GoogleDrive(gauth)

# fileList = drive.ListFile({'q': "'<folder ID>' in parents and trashed=false"}).GetList()
# print(fileList)

def get_children(root_folder_id):
    str = "\'" + root_folder_id + "\'" + " in parents and trashed=false"
    file_list = drive.ListFile({'q': str}).GetList()
    return file_list
def get_folder_id(root_folder_id, root_folder_title):
    file_list = get_children(root_folder_id)
    for file in file_list:
        if(file['title'] == root_folder_title):
            return file['id']
def add_children_to_tree(tree, file_list, parent_id):
    for file in file_list:
        tree.create_node(file['title'], file['id'], parent=parent_id)
        # For debugging
        # print('parent: %s, title: %s, id: %s' % (parent_id, file['title'], file['id']))
### Go down the tree until you reach a leaf ###
def populate_tree_recursively(tree,parent_id):
    children = get_children(parent_id)
    add_children_to_tree(tree, children, parent_id)
    if(len(children) > 0):
        for child in children:
            populate_tree_recursively(tree, child['id'])

## Constant
ROOT_FOLDER_TITLE = "my-top-level-root-folder-name"
ROOT_FOLDER_ID = get_folder_id("root", ROOT_FOLDER_TITLE)
FOLDER_ID = 'Google Drive Folder Id'
FILES = (
    ('file.csv'),
)

tree = Tree()
tree.create_node(ROOT_FOLDER_TITLE, ROOT_FOLDER_ID)
populate_tree_recursively(tree, ROOT_FOLDER_ID)
tree.show()

## Upload file in Google Drive
# file = drive.CreateFile({'title': 'file.csv', "parents": [{"id": FOLDER_ID}]})
# file.SetContentString('TEST')
# file.Upload()

for file_title in FILES :
    file = drive.CreateFile({'title': file_title, "parents": [{"id": FOLDER_ID}]})
    # file.SetContentFile("file.csv") will open the specified file name and set the content of the file to the GoogleDriveFile object. 
    file.SetContentFile(file_title)
    # file.Upload() to complete the upload process.
    file.Upload()
    print('Created file %s with mimeType %s' % (file['title'], file['mimeType']))
    # sleep(10)
    # file.Trash()  # Move file to trash.
    # file.UnTrash()  # Move file out of trash.
    # file.Delete()  # Permanently delete the file.

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from treelib import Node, Tree

# client_secrets.json need to be in the same directory as the script
gauth = GoogleAuth()
# gauth.LocalWebserverAuth() will fire up the browser and ask for your authentication.
# Choose the google account you want o access and authorize the app.
gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth) create a Google Drive object to handle file.
# You will be using this object to list and create file.
drive = GoogleDrive(gauth)

# will get you the list of files/folders in your Google Drive. 
# It will also give you the detail of those files/folders. 
# We capture the folder ID of the folder you would like to upload files to. 
# In this case, file['title'] needs to be match with the folder I would upload the files to.
# View all folders and file in your Google Drive

# helper functions
def get_children(root_folder_id):
    # Build string dynamically (need to use escape characters to support single quote syntax)
    str = "\'" + root_folder_id + "\'" + " in parents and trashed=false"
    # Starting iterating over files
    file_list = drive.ListFile({'q': str}).GetList()
    return file_list

# Retrieve the folder id - start searching from root
# Accessing files in folders
# You can use the ListFile to get the files but this time change the root to file ID.
def get_folder_id(root_folder_id, root_folder_title):
    file_list = get_children(root_folder_id)
    for file in file_list:
        print('Title: %s, ID: %s' % (file['title'], file['id']))
        if(file['title'] == root_folder_title):
            return file['id']

def add_children_to_tree(tree, file_list, parent_id):
    for file in file_list:
        tree.create_node(file['title'], file['id'], parent=parent_id)
        # For debugging
        print('parent: %s, title: %s, id: %s' % (parent_id, file['title'], file['id']))

# Go down the tree until you reach a leaf
def populate_tree_recursively(tree,parent_id):
    children = get_children(parent_id)
    add_children_to_tree(tree, children, parent_id)
    if(len(children) > 0):
        for child in children:
            populate_tree_recursively(tree, child['id'])

# Listing and uploading file in Google Drive
# drive.CreateFile() accepts metadata(dict.) as input to initialize a GoogleDriveFile. 
# I initialized a file with "mimeType" : "text/csv" and "id" : fileID. 
# This id will specific where the file will be uploaded to. 
# In this case, the file will be uploaded to the folder To Share.
def uploadFile(fileID):
    file1 = drive.CreateFile({"mimeType": "text/csv", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
    file1.SetContentFile("local file path")
    # Upload the file.
    file1.Upload()
    print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))   
    # Initialize GoogleDriveFile instance with file id.
    file2 = drive.CreateFile({'id': fileID})
    # Move file to trash
    # Use Trash() to move file to trash.
    file2.Trash()
    # Move file out of trash
    file2.UnTrash()
    # You can also use Delete() to delete the file permanently.
    file2.Delete()

def main():
    # Choose your starting point by inserting file name
    root_folder_title = "my-top-level-root-folder-name"
    root_folder_id = get_folder_id("root", root_folder_title)

    tree = Tree()
    tree.create_node(root_folder_title, root_folder_id)
    populate_tree_recursively(tree, root_folder_id)
    tree.show()

if __name__ == "__main__":
    main()

import time
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up Google Drive API credentials
credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=credentials)

def monitor_drive():
    while True:
        new_files = check_for_new_files()
        for file in new_files:
            sharing_status, changed = determine_sharing_status(file)
            print(f"File: {file['name']}, Sharing Status: {sharing_status}, Changed: {changed}")
        time.sleep(60)  # Adjust the interval as needed


def check_for_new_files():
    response = drive_service.files().list(q="trashed=false",
                                          fields="files(id, name, parents, webViewLink)").execute()
    files = response.get('files', [])
    return files


def determine_sharing_status(file):
    file_id = file['id']
    parents = file.get('parents', [])
    public_folder = False

    # Check if any parent folder is publicly accessible
    for parent_id in parents:
        parent_permissions = drive_service.permissions().list(fileId=parent_id,
                                                              fields="permissions(id, role, type)").execute()
        for permission in parent_permissions.get('permissions', []):
            if permission['role'] == 'reader' and permission['type'] == 'anyone':
                public_folder = True
                break

    # Retrieve current sharing permissions of the file
    file_permissions = drive_service.permissions().list(fileId=file_id,
                                                        fields="permissions(id, role, type)").execute()

    # Check if the file is publicly accessible
    file_public = False
    for permission in file_permissions.get('permissions', []):
        if permission['role'] == 'reader' and permission['type'] == 'anyone':
            file_public = True
            break

    # Change permissions if the file is in a publicly accessible folder
    if public_folder and file_public:
        drive_service.permissions().delete(fileId=file_id, permissionId='anyoneWithLink').execute()
        changed = True
    else:
        changed = False

    return file_public, changed


def retrieve_default_sharing_settings():
    # Retrieve default sharing settings of files
    response = drive_service.files().list(q="trashed=false",
                                          fields="files(id, name, permissions)").execute()
    files = response.get('files', [])
    default_sharing_settings = {}
    for file in files:
        file_id = file['id']
        permissions = file.get('permissions', [])
        default_sharing_settings[file_id] = permissions
    return default_sharing_settings


def main():
    monitor_drive()


if __name__ == "__main__":
    main()

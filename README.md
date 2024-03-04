# README

This script monitors a user's Google Drive, checks for new files, determines their sharing status, and changes permissions if necessary.

## Table of Contents
1. Permissions and Scopes
2. Known Issues
3. Dependencies

---

### 1. Permissions and Scopes

To run the script successfully, the following permissions and scopes are required:

- **Google Drive API Scope**: `https://www.googleapis.com/auth/drive` - This scope allows the script to access files and folders in Google Drive.
- **Google OAuth2 Token**: The script needs authorization to access the user's Google Drive. 

Follow these steps to authorize the script:
1. Run the script: https://script.google.com/home/projects/1QDaGJ13G3za9QVdUjrMXqJKbSE7xyzeY76PVnC614Eq3Y_8M_kgSgj8F/edit 
2. click on "Review Permissions".
3. Sign in to your Google account.
4. Click on "Advanced" under "This app isn't verified".
5. Click on "Go to Public Google Drive files audit (unsafe)".
6. Click "Allow".

### 2. Known Issues

- Currently, the script does not handle shared drives (Team Drives). It only monitors files and folders in a user's personal Google Drive.

### 3. Dependencies

This script has the following dependencies:
- `google-auth` - Authentication library for Google APIs.
- `google-api-python-client` - Client library for accessing Google APIs.
- `google-auth-httplib2` - HTTP library for Google APIs.
- `google-auth-oauthlib` - OAuth library for Google APIs.

Install these dependencies using pip:
```
pip install google-auth google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

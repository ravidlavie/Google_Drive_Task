# README

This script monitors a user's Google Drive, checks for new files, determines their sharing status, and changes permissions if necessary.

## Table of Contents
1. Permissions and Scopes
2. Known Issues
3. Dependencies
4. Usage Examples
5. API Security Considerations

---

### 1. Permissions and Scopes

To run the script successfully, the following permissions and scopes are required:

- **Google Drive API Scope**: `https://www.googleapis.com/auth/drive` - This scope allows the script to access files and folders in Google Drive.
- **Google OAuth2 Token**: The script needs authorization to access the user's Google Drive. 

Follow these steps to authorize the script:
1. Run the script.
2. click on "Review Permissions".
3. Sign in to your Google account.
4. Click on "Advanced" under "This app isn't verified".
5. Click on "Go to Public Google Drive files audit (unsafe)".
6. Click "Allow".

---

### 2. Known Issues

- Currently, the script does not handle shared drives (Team Drives). It only monitors files and folders in a user's personal Google Drive.

---

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
### 4. Usage Examples

To run the script, follow these steps:

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/ravidlavie/Google_Drive_Task/blob/main/monitor_drive.py
    ```

2. Install the required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

3. Ensure you have a `credentials.json` file with the necessary credentials for accessing the Google Drive API. 

4. Run the script using Python:

    ```
    python monitor_drive.py
    ```
 Example Output:

After running the script, you should see output similar to the following:
File: Example.docx, Sharing Status: False, Default Sharing Settings: [{'emailAddress': 'example@gmail.com', 'role': 'writer', 'type': 'user'}], Changed: False

---

### 5. API Security Considerations

"Akamai estimates that roughly 83% of internet traffic is API-based. 
Other studies such as those from Salt Security state that API attacks increased over 600% from 2021 to 2022, and Gartner predicts that 90% of web-enabled applications will have broader attack surfaces due to exposed API’s."

Examples attack surfaces while working with the API:

1. Broken User Authentication: Weak authentication mechanisms, sensitive authentication information in URLs, and credential stuffing can lead to unauthorized access.

2. Excessive Data Exposure: APIs may expose sensitive data in response to user activities, leading to data breaches.

3. Lack of Rate Limiting Controls: Without rate limiting, APIs are vulnerable to denial-of-service attacks, impacting availability and potentially leading to business interruption and loss of revenue.

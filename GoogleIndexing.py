from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from google_auth_httplib2 import AuthorizedHttp
import pandas as pd
import json
import time

# Replace with your JSON key file
JSON_KEY_FILE = "json_key_file_downloaded_after_creating_your_google_service_account_see_above_details_on_how_to_do.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

# Authenticate with Google Service Account
credentials = Credentials.from_service_account_file(JSON_KEY_FILE, scopes=SCOPES)
http = AuthorizedHttp(credentials)

def indexURL(url, http):
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    content = {'url': url.strip(), 'type': "URL_UPDATED"}
    json_ctn = json.dumps(content)

    response, content = http.request(ENDPOINT, method="POST", body=json_ctn, headers={"Content-Type": "application/json"})
    result = json.loads(content.decode())

    if "error" in result:
        print(f"Error({result['error']['code']} - {result['error']['status']}): {result['error']['message']}")
    else:
        print(f"Indexed URL: {result['urlNotificationMetadata']['url']}")
        print(f"Notification Type: {result['urlNotificationMetadata']['latestUpdate']['type']}")
        print(f"Notify Time: {result['urlNotificationMetadata']['latestUpdate']['notifyTime']}")

# Read CSV
csv = pd.read_csv("my_data.csv")
urls = csv["URL"].tolist()

# Process each URL
for url in urls:
    indexURL(url, http)
    time.sleep(1)  # Delay to avoid hitting rate limits

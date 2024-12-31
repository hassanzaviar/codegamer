from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
import pandas as pd
import time

# Replace with your JSON key file
JSON_KEY_FILE = "json_key_file_downloaded_after_creating_your_google_service_account_see_above_details_on_how_to_do.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

# Authenticate
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

def indexURL(url, http):
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    content = {'url': url.strip(), 'type': "URL_UPDATED"}
    json_ctn = json.dumps(content)

    response, content = http.request(ENDPOINT, method="POST", body=json_ctn)
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

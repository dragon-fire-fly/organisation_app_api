from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = "/home/dci-student/Documents/Coding/code_institute/project_5/API/organisation_app_api/client_secret_desktop.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# https://www.youtube.com/watch?v=1JkKtGFnua8&list=PL3JVwFmb_BnTO_sppfTh3VkPhfDWRY5on&index=2
from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = "/home/dci-student/Documents/Coding/code_institute/project_5/API/organisation_app_api/client_secret_desktop.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

request_body = {
    "summary": "Organisation_app events"
}

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


""" To create a calendar: """
# response = service.calendars().insert(body=request_body).execute()
# print(response)

""" To delete a calendar: """
# service.calendars().delete(calendarId="<calender-id-goes-here (e.g. 29pmq8os51p9ens0jrifelloqs@group.calendar.google.com)>").execute()

# response = service.calendarList().list().execute()

# pprint(response)

""" To list calendars """
response = service.calendarList().list(
    maxResults=250,
    showDeleted=False,
    showHidden=False
).execute()

calendarItems = response.get("items")
nextPageToken = response.get("nextPageToken")

while nextPageToken:
    response = service.calendarList().list(
    maxResults=250,
    showDeleted=False,
    showHidden=False
    ).execute()

    calendarItems.extend(response.get("items"))
    nextPageToken = response.get("nextPageToken")

# pprint(calendarItems)

""" Editing calendars"""
""" To filter a specific calendar that contains a search term in summary (title)"""
myCalendar = filter(lambda x: "Organizational" in x["summary"], calendarItems)
myCalendar = next(myCalendar)
print(myCalendar)

# """ Then to edit it """
# myCalendar["summary"] = "Organizational calendar"
# myCalendar["description"] = "Calendar for organizing events"
# myCalendar["location"] = "Essen"

# service.calendars().update(calendarId=myCalendar["id"], body=myCalendar).execute()


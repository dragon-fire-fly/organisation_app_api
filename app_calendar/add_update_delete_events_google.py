from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = "/home/dci-student/Documents/Coding/code_institute/project_5/API/organisation_app_api/client_secret_desktop.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

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

""" To filter a specific calendar that contains a search term in summary (title)"""
myCalendar = filter(lambda x: "Organizational" in x["summary"], calendarItems)
myCalendar = next(myCalendar)
# print(myCalendar)

""" Add, update and delete Events with google calendar API """
#  Obtain the id of the calendar you want to update:
calendar_id = myCalendar["id"]
# print(calendar_id)

"""
Create an event
"""
colors = service.colors().get().execute()
# pprint(colors)

# Optional recurrence value
# recurrence = [
#     "RRULE:FREQ=MONTHLY;COUNT=2"
# ]
hour_adjustment = -2
event_request_body = {
    "start": {
        "dateTime": convert_to_RFC_datetime(2023, 5, 18, 15 + hour_adjustment, 00),
        "timeZone": "(GMT+02:00) Central European Time - Berlin"
        },
    "end": {
        "dateTime": convert_to_RFC_datetime(2023, 5, 18, 23 + hour_adjustment, 00),
        "timeZone": "(GMT+02:00) Central European Time - Berlin"
        },
        "summary": "Dark Troll Festival",
        "description": "Mead drinking and dancing",
        "colorId": 5,
        "status": "confirmed",
        "visibility": "private",
        "location": "Leipzig",
        "attachments": [
            {
                "fileUrl": "https://res.cloudinary.com/djlm3llv5/image/upload/v1683708491/media/images/20230207_220916_cfwfgp.jpg",
                "title": "test pic"
            }
        ],
        "attendees": [
            {
                "displayName": "Kitty",
                "email": "dragon.firefly93@gmail.com",
                "optional": False,
                "organizer": False,
                "responseStatus": "accepted"
            },
            # {
            #     "displayName": "Wolfy",
            #     "optional": False,
            #     "organizer": True,
            #     "responseStatus": "accepted"
            # }
        ],
        # "recurrence": recurrence
}

max_attendees = 5
send_notifications = True
send_updates = "none"
supports_attachments = True

# response = service.events().insert(
#     calendarId = calendar_id,
#     maxAttendees = max_attendees,
#     sendNotifications = send_notifications,
#     sendUpdates = send_updates,
#     supportsAttachments = supports_attachments,
#     body = event_request_body
# ).execute()

# # pprint(response)
# eventId = response["id"]
# print(eventId)

""" Get an event """
event = service.events().get(calendarId=calendar_id, eventId='18ofjhh1a231avhiq4q6lvab7g').execute()

print(event['summary'])


""" Update an event """
start_datetime = convert_to_RFC_datetime(2023, 5, 18, 16 + hour_adjustment, 30)
end_datetime = convert_to_RFC_datetime(2023, 5, 18, 22 + hour_adjustment, 30)
event["start"]["dateTime"] = start_datetime
event["end"]["dateTime"] = end_datetime
event["summary"] = "Dark Troll Festival"
event["description"] = "Music, mead and fun times"
service.events().update(
    calendarId=calendar_id,
    eventId=event["id"],
    body=event).execute()


"""
Delete an event
"""
service.events().delete(calendarId=calendar_id, eventId=event["id"]).execute()
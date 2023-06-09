from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventList.as_view()),
    path("events/<int:pk>/", views.EventDetail.as_view()),
    path("events/<int:pk>/addevent/", views.EventDetailAddEvent.as_view()),
    path("events/calendars/<int:pk>/", views.CalendarEvents.as_view()),
]

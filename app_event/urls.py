from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventList.as_view()),
    path("events/<int:pk>/", views.EventDetail.as_view()),
    path("events/calendar/", views.CalendarEventDetail.as_view()),
]

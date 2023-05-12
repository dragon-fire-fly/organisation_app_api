from django.urls import path
from . import views

urlpatterns = [
    path("calendars/", views.CalendarList.as_view()),
    path("calendar/<int:pk>/", views.CalendarDetail.as_view()),
]

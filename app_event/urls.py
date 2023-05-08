from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventList.as_view()),
    path("event/<int:pk>/", views.EventDetail.as_view()),
    path("events/times/", views.EventTimeList.as_view()),
    path("event/<int:pk>/time/", views.EventTimeDetail.as_view()),
]

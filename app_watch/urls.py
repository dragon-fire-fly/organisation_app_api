from django.urls import path
from . import views

urlpatterns = [
    path("watches/", views.WatchList.as_view()),
    path("watches/<int:pk>/", views.WatchDetail.as_view()),
]

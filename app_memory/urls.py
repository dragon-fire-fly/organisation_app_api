from django.urls import path
from . import views

urlpatterns = [
    path("memories/", views.MemoryList.as_view()),
    path("memories/<int:pk>/", views.MemoryDetail.as_view()),
]

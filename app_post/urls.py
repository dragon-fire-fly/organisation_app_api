from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/create/", views.CreatePost.as_view()),
    path("posts/<int:pk>/edit/", views.UpdatePost.as_view()),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
]

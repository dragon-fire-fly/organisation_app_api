from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="emily", password="password")

    def test_can_list_posts(self):
        emily = User.objects.get(username="emily")
        Post.objects.create(owner=emily, title="a title")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="emily", password="password")
        response = self.client.post("/posts/create/", {"title": "a title"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post("/posts/", {"title": "a title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        emily = User.objects.create_user(username="emily", password="pa$$word")
        chris = User.objects.create_user(username="chris", password="pa$$word")
        Post.objects.create(
            owner=emily, title="a title", content="emilys content"
        )
        Post.objects.create(
            owner=chris, title="another title", content="chris' content"
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.data["title"], "a title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get("/posts/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username="emily", password="pa$$word")
        response = self.client.put("/posts/1/edit/", {"title": "a new title"})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, "a new title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username="emily", password="pa$$word")
        response = self.client.put("/posts/2/edit/", {"title": "a new title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_post(self):
        self.client.login(username="emily", password="pa$$word")
        response = self.client.delete("/posts/1/edit/")
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_another_users_post(self):
        self.client.login(username="emily", password="pa$$word")
        response = self.client.delete("/posts/2/edit/")
        count = Post.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

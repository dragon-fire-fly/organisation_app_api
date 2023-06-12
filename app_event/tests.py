from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username="emily", password="password")
        event = Event.objects.create(
            owner=user,
            title="new event",
            event_type="Educational",
            location="Moon",
            start="2023-06-11 17:00",
            end="2023-06-11 17:00",
            privacy="0",
        )

    def test_can_list_events(self):
        emily = User.objects.get(username="emily")
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="emily", password="password")
        response = self.client.post(
            "/events/",
            {
                "title": "a new title",
                "event_type": "Educational",
                "location": "Moon",
                "start": "2023-06-11 17:00",
                "end": "2023-06-11 17:00",
                "privacy": "0",
            },
        )
        count = Event.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post(
            "/events/",
            {
                "title": "a new title",
                "event_type": "Educational",
                "location": "Moon",
                "start": "2023-06-11 17:00",
                "end": "2023-06-11 17:00",
                "privacy": "0",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        emily = User.objects.create_user(username="emily", password="password")
        chris = User.objects.create_user(username="chris", password="password")
        Event.objects.create(
            owner=emily,
            title="emilys event",
            event_type="Educational",
            location="Moon",
            start="2023-06-11 17:00",
            end="2023-06-11 17:00",
            privacy="0",
        )
        Event.objects.create(
            owner=chris,
            title="chris event",
            event_type="Educational",
            location="Moon",
            start="2023-06-11 17:00",
            end="2023-06-11 17:00",
            privacy="0",
        )

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get("/events/1/")
        self.assertEqual(response.data["title"], "emilys event")
        self.assertEqual(response.data["start"], "2023-06-11 17:00:00")
        self.assertEqual(response.data["past"], True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get("/events/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username="emily", password="password")
        response = self.client.patch("/events/1/", {"title": "a new title"})
        event = Event.objects.filter(pk=1).first()
        self.assertEqual(event.title, "a new title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_event(self):
        self.client.login(username="emily", password="password")
        response = self.client.patch("/events/2/", {"title": "a new title"})
        event = Event.objects.filter(pk=1).first()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cant_update_event(self):
        response = self.client.patch("/events/2/", {"title": "a new title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_event(self):
        self.client.login(username="emily", password="password")
        response = self.client.delete("/events/1/")
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_another_users_event(self):
        self.client.login(username="emily", password="password")
        response = self.client.delete("/events/2/")
        count = Event.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cant_delete_event(self):
        response = self.client.delete("/events/2/")
        count = Event.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

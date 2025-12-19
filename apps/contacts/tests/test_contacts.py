import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from apps.contacts.models import Contact, Tag


User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='password123')

@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def contact(db, user):
    return Contact.objects.create(
        name='John Doe',
        email='john@example.com',
        phone_number='998901234560',
        user=user
    )

@pytest.fixture
def tag(db, contact):
    return Tag.objects.create(
        name='Friend',
        contacts=contact
    )


def test_create_contact(authenticated_client):
    url = reverse('contact-create')
    data = {"name": "Alice", "email": "alice@example.com", "phone_number": "998901234569"}
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == "Alice"


def test_update_contact(authenticated_client, contact):
    url = reverse('contact-update-destroy', args=[contact.id])
    data = {"name": "Updated Name"}
    response = authenticated_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == "Updated Name"


def test_delete_contact(authenticated_client, contact):
    url = reverse('contact-update-destroy', args=[contact.id])
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_create_tag(authenticated_client, contact):
    url = reverse('tag-create')
    data = {
        "name": "Colleague",
        "contacts": contact.id
    }
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == "Colleague"


def test_delete_tag(authenticated_client, tag):
    url = reverse('tag-destroy', args=[tag.id])
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_list_tags(authenticated_client, tag):
    url = reverse('tag-list')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) >= 1


def test_search_contact(authenticated_client, contact):
    url = reverse('contact-search')
    response = authenticated_client.get(url, {"search": "John"})
    assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def user1(db):
    return User.objects.create_user(username="user1", password="pass123")


@pytest.fixture
def user2(db):
    return User.objects.create_user(username="user2", password="pass123")


@pytest.fixture
def contact_user1(db, user1):
    return Contact.objects.create(
        user=user1,
        name="John User1",
        email="john1@test.com",
        phone_number="+998901234567"
    )


@pytest.fixture
def contact_user2(db, user2):
    return Contact.objects.create(
        user=user2,
        name="John User2",
        email="john2@test.com",
        phone_number="+998901234568"
    )


def test_user_can_only_see_own_contacts(
    api_client,
    user1,
    contact_user1,
    contact_user2
    ):
    api_client.force_authenticate(user=user1)

    url = reverse("contact-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    returned_ids = [c["id"] for c in response.data]

    assert contact_user1.id in returned_ids

    assert contact_user2.id not in returned_ids

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from advanced_hello_world_core.models import Message


@pytest.mark.django_db
def test_message_is_trimmed_and_saved() -> None:
    response = APIClient().post(
        reverse("advanced_hello_world_core:messages"),
        {"text": "  Hello from a test  "},
        format="json",
    )

    assert response.status_code == 201
    assert response.json()["text"] == "Hello from a test"
    assert Message.objects.get().text == "Hello from a test"


@pytest.mark.django_db
def test_blank_message_is_rejected() -> None:
    response = APIClient().post(
        reverse("advanced_hello_world_core:messages"), {"text": "   "}, format="json"
    )

    assert response.status_code == 400
    assert Message.objects.count() == 0


@pytest.mark.django_db
def test_messages_are_listed_newest_first() -> None:
    Message.objects.create(text="First")
    Message.objects.create(text="Second")

    response = APIClient().get(reverse("advanced_hello_world_core:messages"))

    assert response.status_code == 200
    assert [item["text"] for item in response.json()] == ["Second", "First"]


@pytest.mark.django_db
def test_health_endpoints() -> None:
    client = APIClient()

    assert client.get(reverse("advanced_hello_world_core:liveness")).json() == {"status": "ok"}
    assert client.get(reverse("advanced_hello_world_core:readiness")).json() == {"status": "ready"}

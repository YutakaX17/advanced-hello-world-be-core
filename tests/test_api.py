import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_health_endpoints() -> None:
    client = Client()

    assert client.get(reverse("advanced_hello_world_core:liveness")).json() == {"status": "ok"}
    assert client.get(reverse("advanced_hello_world_core:readiness")).json() == {"status": "ready"}

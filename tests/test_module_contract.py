import pytest

from advanced_hello_world_core.module import BackendModule


def test_backend_module_accepts_declarative_metadata() -> None:
    module = BackendModule(
        id="messages",
        django_app="advanced_hello_world_messages",
        urls="advanced_hello_world_messages.urls",
    )

    assert module.id == "messages"
    assert module.url_prefix == "api/"


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("id", "Messages"),
        ("django_app", "invalid-path"),
        ("urls", "invalid-path"),
        ("url_prefix", "/api/"),
    ],
)
def test_backend_module_rejects_invalid_metadata(field: str, value: str) -> None:
    values = {
        "id": "messages",
        "django_app": "advanced_hello_world_messages",
        "urls": "advanced_hello_world_messages.urls",
        "url_prefix": "api/",
    }
    values[field] = value

    with pytest.raises(ValueError):
        BackendModule(**values)

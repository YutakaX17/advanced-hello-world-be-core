import pytest
from django.db import connection
from django.db.migrations.executor import MigrationExecutor


@pytest.mark.django_db(transaction=True)
def test_message_table_and_existing_rows_survive_state_release() -> None:
    executor = MigrationExecutor(connection)
    executor.migrate([("advanced_hello_world_core", "0001_initial")])
    old_apps = executor.loader.project_state([("advanced_hello_world_core", "0001_initial")]).apps
    old_message = old_apps.get_model("advanced_hello_world_core", "Message")
    existing = old_message.objects.create(text="Preserve me")

    executor = MigrationExecutor(connection)
    executor.migrate([("advanced_hello_world_core", "0002_release_message_state")])

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT text FROM advanced_hello_world_core_message WHERE id = %s",
            [existing.pk.hex],
        )
        assert cursor.fetchone() == ("Preserve me",)

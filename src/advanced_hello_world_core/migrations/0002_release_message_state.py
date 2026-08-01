from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("advanced_hello_world_core", "0001_initial")]
    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[migrations.DeleteModel(name="Message")],
            database_operations=[],
        )
    ]

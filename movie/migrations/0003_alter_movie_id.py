# Generated by Django 4.2.4 on 2023-08-16 12:26

# Python imports
import uuid

# Django imports
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0002_alter_screenseattypesmapping_seat_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
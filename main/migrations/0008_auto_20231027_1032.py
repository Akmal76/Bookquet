# Generated by Django 4.2.6 on 2023-10-27 03:32

from django.db import migrations
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books.json")

class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_auto_20231027_1020"),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
# Generated by Django 4.2.6 on 2023-10-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_book_rate_alter_comment_buku_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="rated_books",
            field=models.ManyToManyField(related_name="rated_books", to="main.book"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="read_later_books",
            field=models.ManyToManyField(
                related_name="read_later_books", to="main.book"
            ),
        ),
    ]

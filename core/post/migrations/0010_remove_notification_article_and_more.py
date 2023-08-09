# Generated by Django 4.1.7 on 2023-06-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0009_notification"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="article",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="notification_type",
        ),
        migrations.AddField(
            model_name="notification",
            name="description",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="notification",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
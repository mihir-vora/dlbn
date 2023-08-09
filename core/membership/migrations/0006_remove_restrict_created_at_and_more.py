# Generated by Django 4.1.7 on 2023-06-08 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("membership", "0005_alter_restrict_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="restrict",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="restrict",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="restrict",
            name="plan",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="membership.plan",
            ),
        ),
    ]

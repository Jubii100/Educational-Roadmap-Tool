# Generated by Django 4.2.2 on 2023-07-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roadmaps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roadmapcateg",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

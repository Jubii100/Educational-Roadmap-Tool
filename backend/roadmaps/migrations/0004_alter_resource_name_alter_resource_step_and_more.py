# Generated by Django 4.2.2 on 2023-07-12 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("roadmaps", "0003_rename_creator_roadmap_creator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="resource",
            name="step",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resources",
                to="roadmaps.roadmapstep",
            ),
        ),
        migrations.AlterField(
            model_name="roadmap",
            name="creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="roadmaps",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="roadmap",
            name="title",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="roadmapstep",
            name="name",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="roadmapstep",
            name="roadmap",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="steps",
                to="roadmaps.roadmap",
            ),
        ),
    ]
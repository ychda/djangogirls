# Generated by Django 1.11.5 on 2017-12-16 21:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        ("applications", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="score",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="scores", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="form",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="applications.Form"),
        ),
        migrations.AddField(
            model_name="form",
            name="event",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="core.Event"),
        ),
        migrations.AddField(
            model_name="email",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="author", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="email",
            name="form",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="applications.Form"),
        ),
        migrations.AddField(
            model_name="application",
            name="form",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="applications.Form"),
        ),
        migrations.AddField(
            model_name="answer",
            name="application",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="applications.Application"),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="applications.Question"),
        ),
        migrations.AlterUniqueTogether(
            name="score",
            unique_together={("user", "application")},
        ),
        migrations.AlterUniqueTogether(
            name="application",
            unique_together={("form", "email")},
        ),
    ]

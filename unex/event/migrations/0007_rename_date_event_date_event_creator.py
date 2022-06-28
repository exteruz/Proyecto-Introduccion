# Generated by Django 4.0.5 on 2022-06-28 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0006_remove_event_creator_remove_event_date_event_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]

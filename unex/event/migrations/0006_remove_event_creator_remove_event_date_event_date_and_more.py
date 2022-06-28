# Generated by Django 4.0.5 on 2022-06-28 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='hour',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-09 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_category_event_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['name'], 'verbose_name': 'event'},
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../images'),
        ),
    ]

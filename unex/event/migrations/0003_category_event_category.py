# Generated by Django 4.0.5 on 2022-06-09 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(to='event.category'),
        ),
    ]

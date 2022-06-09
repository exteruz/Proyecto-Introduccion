# Generated by Django 4.0.5 on 2022-06-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('Description', models.TextField(max_length=245)),
                ('facultad', models.CharField(blank=True, max_length=20, null=True)),
                ('undergrade', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('place', models.CharField(max_length=200)),
                ('points', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]

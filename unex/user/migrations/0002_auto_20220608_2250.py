# Generated by Django 3.1.7 on 2022-06-09 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_insignia_alter_rango_options_reward'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='insignia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='points.insignia'),
        ),
        migrations.AddField(
            model_name='user',
            name='rango',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='points.rango'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-16 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_insignia_alter_rango_options_reward'),
        ('event', '0004_alter_category_options_alter_event_options_and_more'),
        ('user', '0002_auto_20220608_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('change_task_status', 'Can change the status of tasks'), ('close_task', 'Can remove a task by setting its status as closed')]},
        ),
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.ManyToManyField(blank=True, to='event.category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='event',
            field=models.ManyToManyField(blank=True, to='event.event'),
        ),
        migrations.AlterField(
            model_name='user',
            name='faculty',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='insignia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='points.insignia'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, max_length=123, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pregrado',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rango',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='points.rango'),
        ),
        migrations.AlterField(
            model_name='user',
            name='reward',
            field=models.ManyToManyField(blank=True, to='points.reward'),
        ),
    ]
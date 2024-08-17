# Generated by Django 4.2.15 on 2024-08-17 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorial', '0002_remove_tutorial_date_remove_tutorial_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_date',
        ),
        migrations.CreateModel(
            name='TutorialDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_tutorial_date', to='tutorial.tutorial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutorial_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.tutorialdate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

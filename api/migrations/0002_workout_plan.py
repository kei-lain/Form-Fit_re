# Generated by Django 4.2.6 on 2023-11-09 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_person_password'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planName', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.person')),
                ('workouts', models.ManyToManyField(to='api.workout')),
            ],
        ),
    ]
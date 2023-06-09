# Generated by Django 4.1.5 on 2023-03-28 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('from_var', models.CharField(max_length=100)),
                ('to_var', models.CharField(max_length=100)),
                ('trip_for', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('remaining_time', models.CharField(max_length=100)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

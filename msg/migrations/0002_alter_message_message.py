# Generated by Django 4.1.5 on 2023-03-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=1500),
        ),
    ]

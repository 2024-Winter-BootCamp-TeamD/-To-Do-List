# Generated by Django 5.1.4 on 2024-12-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]

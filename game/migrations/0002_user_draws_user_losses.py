# Generated by Django 5.1.3 on 2024-12-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='draws',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='losses',
            field=models.IntegerField(default=0),
        ),
    ]

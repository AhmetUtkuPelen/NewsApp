# Generated by Django 5.0.4 on 2024-04-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0003_createnews_creation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='createnews',
            name='approx_read_time',
            field=models.IntegerField(default=0),
        ),
    ]

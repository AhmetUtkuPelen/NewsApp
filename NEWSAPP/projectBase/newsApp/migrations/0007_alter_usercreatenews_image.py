# Generated by Django 5.0.4 on 2024-04-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0006_usercreatenews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreatenews',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]

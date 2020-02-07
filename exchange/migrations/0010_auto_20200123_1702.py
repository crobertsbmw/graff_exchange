# Generated by Django 3.0.1 on 2020-01-23 17:02

from django.db import migrations
import exchange.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0009_auto_20200123_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sketch',
            name='image',
            field=stdimage.models.JPEGField(upload_to=exchange.models.upload_to),
        ),
    ]
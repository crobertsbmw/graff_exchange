# Generated by Django 3.0.1 on 2020-01-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_auto_20200121_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='can_post_to_reddit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

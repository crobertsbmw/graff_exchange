# Generated by Django 3.0.1 on 2020-01-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0011_signup_exchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='moniker',
        ),
        migrations.AddField(
            model_name='signup',
            name='tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

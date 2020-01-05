# Generated by Django 3.0.1 on 2020-01-05 21:31

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import exchange.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('points', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('moniker', models.CharField(max_length=255)),
                ('write_style', models.CharField(blank=True, choices=[('handstyle', 'handstyle'), ('wildstyle', 'wildstyle'), ('throwie', 'throwie'), ('keyboard', 'keyboard'), ('piece', 'piece')], max_length=255, null=True)),
                ('recieve_style', models.CharField(blank=True, choices=[('handstyle', 'handstyle'), ('wildstyle', 'wildstyle'), ('throwie', 'throwie'), ('keyboard', 'keyboard'), ('piece', 'piece')], max_length=255, null=True)),
                ('do_double', models.BooleanField(default=False)),
                ('comments', models.CharField(blank=True, max_length=1200, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(blank=True, choices=[('handstyle', 'handstyle'), ('wildstyle', 'wildstyle'), ('throwie', 'throwie'), ('keyboard', 'keyboard'), ('piece', 'piece')], max_length=255, null=True)),
                ('rematch', models.BooleanField(default=False)),
                ('moniker', models.CharField(max_length=255)),
                ('password', models.CharField(default=exchange.models.rand_string, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sketch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='%Y/%m/%d/')),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('assignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sketches', to='exchange.Assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=exchange.models.month_year_string, max_length=255)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='exchange',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', related_query_name='assignment', to='exchange.Exchange'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', related_query_name='assignment', to=settings.AUTH_USER_MODEL),
        ),
    ]

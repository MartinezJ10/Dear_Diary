# Generated by Django 3.1 on 2020-08-29 19:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0005_auto_20200829_1312'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserClient',
        ),
    ]

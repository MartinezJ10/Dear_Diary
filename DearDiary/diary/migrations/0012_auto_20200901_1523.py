# Generated by Django 3.1 on 2020-09-01 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0011_auto_20200901_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarypage',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diary.customer'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-21 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_ID',
        ),
    ]
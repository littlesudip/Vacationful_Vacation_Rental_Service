# Generated by Django 3.1.1 on 2020-09-29 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='City',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='First_Name',
            new_name='Full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Last_Name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='State',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Street_Address',
        ),
    ]

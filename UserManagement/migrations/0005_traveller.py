# Generated by Django 2.2 on 2020-09-21 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0004_delete_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelling_area', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserManagement.User')),
            ],
        ),
    ]
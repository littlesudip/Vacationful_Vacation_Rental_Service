# Generated by Django 3.1.1 on 2020-09-29 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0001_initial'),
        ('PropertyManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Owner.owner'),
        ),
    ]

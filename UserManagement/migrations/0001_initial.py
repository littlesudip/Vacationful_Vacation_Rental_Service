# Generated by Django 3.1.1 on 2020-09-28 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=200)),
                ('Street_Address', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('City', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('State', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('Country', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('Contact_No', models.IntegerField(blank=True, default='', null=True)),
                ('Profile_Picture', models.ImageField(blank=True, default='users/pro_pics/default.jpg', null=True, upload_to='images/pro_pic')),
                ('NID_No', models.IntegerField(blank=True, default='', null=True)),
                ('NID_Front', models.ImageField(blank=True, default='images/idcard/front.jpg', null=True, upload_to='images/idcard')),
                ('NID_Back', models.ImageField(blank=True, default='images/idcard/back.jpg', null=True, upload_to='images/idcard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

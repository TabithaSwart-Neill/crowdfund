# Generated by Django 3.0.8 on 2020-09-24 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_middle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
    ]

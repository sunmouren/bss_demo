# Generated by Django 2.1.7 on 2019-04-02 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190402_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='following_users',
        ),
    ]

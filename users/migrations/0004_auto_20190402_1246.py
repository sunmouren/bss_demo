# Generated by Django 2.1.7 on 2019-04-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190331_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='image/default_avatar.png', upload_to='image/user/avatar', verbose_name='头像'),
        ),
    ]

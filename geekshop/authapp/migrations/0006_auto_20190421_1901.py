# Generated by Django 2.1.8 on 2019-04-21 19:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20190420_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='vk_link',
            field=models.TextField(blank=True, verbose_name='VK страница'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 23, 19, 1, 9, 999818, tzinfo=utc)),
        ),
    ]
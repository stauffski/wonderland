# Generated by Django 2.2.1 on 2019-05-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20190526_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tracks',
        ),
        migrations.AddField(
            model_name='event',
            name='tracks',
            field=models.ManyToManyField(to='records.Track'),
        ),
    ]

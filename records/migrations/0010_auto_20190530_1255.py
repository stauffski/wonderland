# Generated by Django 2.2.1 on 2019-05-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_racer_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racer',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='records.Sponsor'),
        ),
    ]

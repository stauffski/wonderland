# Generated by Django 2.2.1 on 2019-06-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0030_auto_20190618_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

# Generated by Django 3.2.2 on 2021-06-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minesite', '0018_auto_20210615_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightdetails',
            name='status',
            field=models.CharField(default='CONFIRMED', max_length=12),
        ),
    ]

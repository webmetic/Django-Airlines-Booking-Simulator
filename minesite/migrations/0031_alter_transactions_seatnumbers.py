# Generated by Django 3.2.2 on 2021-06-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minesite', '0030_auto_20210617_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='seatnumbers',
            field=models.CharField(default='', max_length=4),
        ),
    ]

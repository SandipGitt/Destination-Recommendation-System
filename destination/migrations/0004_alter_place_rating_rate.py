# Generated by Django 3.2.11 on 2022-01-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0003_auto_20220126_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place_rating',
            name='rate',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0022_alter_profile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(max_length=15),
        ),
    ]
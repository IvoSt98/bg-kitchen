# Generated by Django 4.2.16 on 2024-11-18 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_reservations_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='name_2',
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0040_auto_20201128_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='creator_community_id',
        ),
    ]
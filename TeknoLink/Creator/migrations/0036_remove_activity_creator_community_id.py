# Generated by Django 3.1.1 on 2020-11-28 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0035_auto_20201128_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='creator_community_id',
        ),
    ]
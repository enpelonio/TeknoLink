# Generated by Django 3.1.1 on 2020-11-18 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0003_auto_20201118_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='isTask',
        ),
    ]
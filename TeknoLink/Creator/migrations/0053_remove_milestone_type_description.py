# Generated by Django 3.1.1 on 2020-11-29 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0052_remove_milestone_milestone_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milestone_type',
            name='description',
        ),
    ]
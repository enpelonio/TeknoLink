# Generated by Django 3.1.1 on 2020-11-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0004_remove_activity_istask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(),
        ),
    ]

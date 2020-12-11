# Generated by Django 3.1.1 on 2020-12-08 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0073_auto_20201208_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_schedule_pattern',
            name='onWednesDay',
        ),
        migrations.AddField(
            model_name='event_schedule_pattern',
            name='onWednesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event_schedule_pattern',
            name='onFriday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event_schedule_pattern',
            name='onMonday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event_schedule_pattern',
            name='onSaturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event_schedule_pattern',
            name='onSunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event_schedule_pattern',
            name='onThursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event_schedule_pattern',
            name='onTuesday',
            field=models.BooleanField(default=False),
        ),
    ]
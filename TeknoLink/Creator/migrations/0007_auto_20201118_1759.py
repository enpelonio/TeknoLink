# Generated by Django 3.1.1 on 2020-11-18 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0006_auto_20201118_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_schedule_pattern',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.activity'),
        ),
    ]

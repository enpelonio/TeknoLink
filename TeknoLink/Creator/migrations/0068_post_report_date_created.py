# Generated by Django 3.1.1 on 2020-11-30 03:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0067_student_post_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_report',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
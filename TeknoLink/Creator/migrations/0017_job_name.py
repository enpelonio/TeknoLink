# Generated by Django 3.1.1 on 2020-11-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0016_milestone_type_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
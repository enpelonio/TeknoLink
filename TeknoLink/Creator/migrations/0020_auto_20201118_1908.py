# Generated by Django 3.1.1 on 2020-11-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0019_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community_improve_skill',
            name='skill_points_per_week',
        ),
        migrations.AddField(
            model_name='community_improve_skill',
            name='skill_percentage_boost',
            field=models.DecimalField(decimal_places=2, default=0.05, max_digits=5),
        ),
    ]

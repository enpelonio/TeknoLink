# Generated by Django 3.1.1 on 2020-11-28 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0037_activity_creator_community_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='creator_community_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_creator_id', to='Creator.community'),
        ),
    ]

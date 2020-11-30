# Generated by Django 3.1.1 on 2020-11-28 10:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0036_remove_activity_creator_community_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='creator_community_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='activity_creator_id', to='Creator.community'),
            preserve_default=False,
        ),
    ]
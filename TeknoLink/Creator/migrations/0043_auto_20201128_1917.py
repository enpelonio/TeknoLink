# Generated by Django 3.1.1 on 2020-11-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0042_activity_creator_community_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='create_admin_id',
        ),
        migrations.RemoveField(
            model_name='community',
            name='delete_admin_id',
        ),
        migrations.RemoveField(
            model_name='community_improve_skill',
            name='community_id',
        ),
        migrations.RemoveField(
            model_name='community_member',
            name='community_id',
        ),
        migrations.RemoveField(
            model_name='student_community_subscription',
            name='community_id',
        ),
    ]

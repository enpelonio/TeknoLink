# Generated by Django 3.1.1 on 2020-11-30 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0062_remove_student_possess_skill_points_to_next_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Post_Type',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]

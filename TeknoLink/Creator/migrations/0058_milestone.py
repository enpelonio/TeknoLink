# Generated by Django 3.1.1 on 2020-11-29 07:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0057_delete_milestone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_acquired', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('directlink', models.TextField()),
                ('milestone_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('milestone_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.milestone_type')),
                ('owner_student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.student')),
            ],
            options={
                'db_table': 'Milestone',
            },
        ),
    ]
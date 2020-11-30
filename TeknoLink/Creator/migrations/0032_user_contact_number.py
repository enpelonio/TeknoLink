# Generated by Django 3.1.1 on 2020-11-28 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0031_delete_user_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Contact_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Creator.user')),
            ],
            options={
                'db_table': 'User_Contact_Number',
            },
        ),
    ]
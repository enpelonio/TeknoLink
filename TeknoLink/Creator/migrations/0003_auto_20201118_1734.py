# Generated by Django 3.1.1 on 2020-11-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Creator', '0002_auto_20201118_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='create_admin_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_admin_id_set', to='Creator.community'),
        ),
    ]
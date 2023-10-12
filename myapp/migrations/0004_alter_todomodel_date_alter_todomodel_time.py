# Generated by Django 4.2.6 on 2023-10-12 07:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_todomodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20200407_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations_visited',
            name='case_no',
        ),
        migrations.AddField(
            model_name='locations_visited',
            name='case_no',
            field=models.ManyToManyField(to='patients.Patients'),
        ),
    ]
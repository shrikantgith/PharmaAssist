# Generated by Django 3.0.6 on 2021-03-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Medicine',
        ),
        migrations.AddField(
            model_name='patient',
            name='medicine',
            field=models.ManyToManyField(to='medical.Medicine'),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-16 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0003_candidate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]

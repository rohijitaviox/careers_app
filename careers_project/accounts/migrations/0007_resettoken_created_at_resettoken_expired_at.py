# Generated by Django 4.1.4 on 2022-12-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resettoken',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='resettoken',
            name='expired_at',
            field=models.DateTimeField(null=True),
        ),
    ]

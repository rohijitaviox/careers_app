# Generated by Django 4.1.4 on 2022-12-15 04:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resettoken',
            name='token',
        ),
        migrations.AlterField(
            model_name='resettoken',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-17 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='lastname',
        ),
    ]

# Generated by Django 4.1.5 on 2023-06-23 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0010_delete_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Pluses',
        ),
    ]
# Generated by Django 4.1.5 on 2023-06-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_exp_feild'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exp',
            old_name='Employee',
            new_name='emp',
        ),
    ]

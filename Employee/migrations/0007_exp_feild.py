# Generated by Django 4.1.5 on 2023-06-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0006_exp_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='exp',
            name='feild',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
# Generated by Django 4.1.5 on 2023-06-19 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0006_alter_experience_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.TextField(max_length=500, null=True),
        ),
    ]

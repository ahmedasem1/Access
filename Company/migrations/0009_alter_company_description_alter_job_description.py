# Generated by Django 4.1.5 on 2023-06-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0008_alter_job_description_alter_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]

# Generated by Django 4.1.5 on 2023-06-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0007_alter_company_description_alter_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

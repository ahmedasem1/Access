# Generated by Django 4.1.5 on 2023-06-19 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_remove_job_hours_remove_job_salary_alter_job_pluses'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]

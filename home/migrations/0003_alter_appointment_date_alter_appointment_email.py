# Generated by Django 4.2.7 on 2024-01-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_date_time_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
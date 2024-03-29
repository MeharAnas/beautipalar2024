# Generated by Django 4.2.7 on 2024-01-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_appointment_date_alter_appointment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Message',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Number',
            field=models.CharField(max_length=20),
        ),
    ]

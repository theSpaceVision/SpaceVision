# Generated by Django 4.1.7 on 2023-04-23 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_eiadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eiadata',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
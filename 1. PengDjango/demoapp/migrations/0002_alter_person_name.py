# Generated by Django 4.1.7 on 2023-03-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Name',
            field=models.CharField(max_length=30),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='balance',
            field=models.PositiveIntegerField(),
        ),
    ]

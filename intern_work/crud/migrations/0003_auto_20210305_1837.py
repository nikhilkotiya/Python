# Generated by Django 3.1.7 on 2021-03-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210305_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]

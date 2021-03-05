# Generated by Django 3.1.7 on 2021-03-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=40)),
                ('amount', models.PositiveIntegerField(max_length=2147483647)),
                ('balance', models.PositiveIntegerField(max_length=2147483647)),
                ('txn_type', models.CharField(max_length=60)),
                ('txn_info', models.CharField(max_length=60)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='price',
            field=models.IntegerField(default=1000),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='battary_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.IntegerField(),
        ),
    ]

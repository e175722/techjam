# Generated by Django 2.2.11 on 2020-03-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20200319_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='introduction_1',
            field=models.TextField(default='', max_length=255, verbose_name='社歴'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='introduction_2',
            field=models.TextField(default='', max_length=255, verbose_name='アピール'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='introduction_3',
            field=models.TextField(default='', max_length=255, verbose_name='紹介'),
        ),
    ]

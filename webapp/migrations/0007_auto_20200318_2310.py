# Generated by Django 2.2.11 on 2020-03-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_employee_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_by',
            field=models.CharField(default='', max_length=255, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(default='', max_length=255, verbose_name='所属'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default='', max_length=255, verbose_name='社員id'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joined_at',
            field=models.CharField(default='', max_length=255, verbose_name='入社年度'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mail',
            field=models.EmailField(default='', max_length=255, verbose_name='メール'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='名前'),
        ),
    ]

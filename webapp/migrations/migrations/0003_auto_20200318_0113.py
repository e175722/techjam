# Generated by Django 2.2.11 on 2020-03-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200318_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagcategory',
            name='category',
            field=models.CharField(max_length=255, verbose_name='タグ名前'),
        ),
        migrations.AlterField(
            model_name='tagcategory',
            name='tag_id',
            field=models.IntegerField(verbose_name='タグid'),
        ),
    ]
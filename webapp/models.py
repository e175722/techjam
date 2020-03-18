from django.db import models
from django.utils import timezone
from django_mysql.models import Model, JSONField

class Employee(Model, models.Model):
    employee_id = models.CharField('社員id',max_length=255,default='')
    name = models.CharField('名前',max_length=255,default='')
    department = models.CharField('所属',max_length=255,default='')
    tag = JSONField('タグ')
    introduction = JSONField('紹介文')
    mail = models.EmailField('メール',max_length=255, default='')
    img_url = models.FileField(upload_to='upload/',default='')
    joined_at = models.CharField('入社年度',max_length=255,default='')
    created_by = models.CharField('作成者',max_length=255,default='')
    created_at = models.DateTimeField('作成日時',default=timezone.now)
    updated_at = models.DateTimeField('更新日時',default=timezone.now)


class Admin(Model,models.Model):
    name = models.CharField('名前',max_length=255)
    employee_id = models.CharField('社員id',max_length=255)
    password =  models.CharField('社員id',max_length=255)


class TagCategory(Model,models.Model):
    tag_id = models.IntegerField('タグid')
    category = models.CharField('タグ名前',max_length=255)

class IntroductionCategory(Model,models.Model):
    category_id = models.IntegerField('カテゴリーid')
    category_name = models.CharField('カテゴリーの名前',max_length=255)


class FileModel(models.Model):
    title = models.CharField(max_length=100)
    uploadplace = models.FileField(upload_to='upload/')

from django.db import models
from django.utils import timezone
from django_mysql.models import Model, JSONField

class Employee(Model, models.Model):
    employee_id = models.CharField('社員id',max_length=255)
    name = models.CharField('名前',max_length=255)
    department = models.CharField('所属',max_length=255)
    tag = JSONField('タグ')
    introduction = JSONField('紹介文')
    mail = models.EmailField('メール',max_length=255)
    joined_at = models.CharField('入社年度',max_length=255)
    created_by = models.CharField('作成者',max_length=255)
    created_at = models.DateTimeField('作成日時',default=timezone.now)
    updated_at = models.DateTimeField('更新日時',default=timezone.now)


class Admin(Model,models.Model):
    name = models.CharField('名前',max_length=255)
    employee_id = models.CharField('社員id',max_length=255)
    password =  models.CharField('社員id',max_length=255)


class TagCategory(Model,models.Model):
    tag_id = JSONField('タグ')
    category = JSONField('タグ')

class IntroductionCategory(Model,models.Model):
    category_id = models.IntegerField('カテゴリーid')
    category_name = models.CharField('カテゴリーの名前',max_length=255)

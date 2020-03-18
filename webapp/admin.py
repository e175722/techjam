from django.contrib import admin
from webapp.models import Employee, Admin, TagCategory, IntroductionCategory

admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(TagCategory)
admin.site.register(IntroductionCategory)


# Register your models here.

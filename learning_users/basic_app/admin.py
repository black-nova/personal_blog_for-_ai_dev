from django.contrib import admin
from basic_app.models import userprofileinfo
# Register your models here.
from django.contrib import admin
from .models import Task
from .models import Task1


admin.site.register(Task)
admin.site.register(Task1)
admin.site.register(userprofileinfo)

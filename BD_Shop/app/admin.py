from django.contrib import admin
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]
  

    class Meta:
        model = Department

admin.site.register(Department, DepartmentAdmin)
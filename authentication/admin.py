from django.contrib import admin

# Register your models here.
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "created_at"]


admin.site.register(Employee, EmployeeAdmin)

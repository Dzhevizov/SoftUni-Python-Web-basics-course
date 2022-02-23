from django.contrib import admin

from employee_app.employee.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'job_title', 'company')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

from django import template

from employee_app.employee.models import Department

register = template.Library()


@register.inclusion_tag('tags/department_list.html')
def department_list():
    departments = Department.objects.prefetch_related('employee_set').all()

    return {
        'departments': departments
    }

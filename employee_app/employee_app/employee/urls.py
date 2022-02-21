from django.urls import path

from employee_app.employee.views import list_departments, department_details, not_found

urlpatterns = (
    path('', list_departments, name='list departments'),
    path('<int:dep_id>/', department_details, name='department details'),
    path('not-found', not_found, name='not found')
)

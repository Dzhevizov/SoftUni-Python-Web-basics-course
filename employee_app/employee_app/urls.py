from django.contrib import admin
from django.urls import path, include

from employee_app.employee.views import home, go_to_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('go-to-home', go_to_home, name='go to home'),
    path('departments/', include('employee_app.employee.urls')),
    path('templates/', include('employee_app.template_examples.urls')),
]

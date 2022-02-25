from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from employee_app.employee.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    # path('go-to-home', go_to_home, name='go to home'),
    # path('departments/', include('employee_app.employee.urls')),
    path('templates/', include('employee_app.template_examples.urls')),
    path('employees/', include('employee_app.employee.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



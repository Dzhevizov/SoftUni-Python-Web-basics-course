from django.urls import path

from employee_app.template_examples.views import index

urlpatterns = (
    path('', index, name='templates index'),
)

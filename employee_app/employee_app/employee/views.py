import random

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# def home(request):
#     html = f'<h1>{request.method}: This is home</h1>'
#     return HttpResponse(
#         html,
#         # content_type='text/plain',
#     )
from django.urls import reverse_lazy

from employee_app.employee.models import Department, Employee


def home(request):

    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('department details', kwargs={
        'dep_id': 2,
    }))
    print(reverse_lazy('not found'))

    context = {
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for _ in range(16)],
    }
    return render(request, 'index.html', context, content_type='text/html')


def not_found(request):
    # return HttpResponseNotFound()
    raise Http404


def go_to_home(request):
    return redirect('department details', dep_id=random.randint(1, 1024))


def department_details(request, dep_id):
    return HttpResponse(f'This is department {dep_id}')


def list_departments(request):
    department = Department(
        name=f'Department {random.randint(1, 1024)}',
    )
    department.save()
    Department.objects.create(
        name=f'Department {random.randint(1, 1024)}',
    )

    print(list(Department.objects.filter(name='TV App')))
    print(Department.objects.get(name='TV App'))

    context = {
        'departments': Department.objects.prefetch_related('employee_set').all(),
        'employees': Employee.objects.all()
    }
    return render(request, 'list_of_departments.html', context)


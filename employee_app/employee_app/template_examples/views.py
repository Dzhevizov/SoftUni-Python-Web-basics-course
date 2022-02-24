from django.shortcuts import render

from employee_app.employee.models import Employee, Department


def index(request):
    context = {
        'num_1': 123,
        'num_2': 200,
        'num_3': 321,
        'numbers': [123, 200, 321],
        'filesize': 123456789,
        'title': 'emplOYees LIst',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aliquid asperiores aut corporis cumque debitis ea eum iste iusto maxime minus, modi mollitia nostrum obcaecati optio qui saepe sed sit!',
        'employees': Employee.objects.order_by('first_name', 'last_name').all(),
        'departments_names': [d.name for d in Department.objects.all()]
    }
    return render(request, 'template_examples/index.html', context)


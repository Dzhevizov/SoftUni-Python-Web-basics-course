import random

from django import forms
from django.core.exceptions import ValidationError
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


# def home(request):
#
#     print(reverse_lazy('index'))
#     print(reverse_lazy('go to home'))
#     print(reverse_lazy('list departments'))
#     print(reverse_lazy('department details', kwargs={
#         'dep_id': 2,
#     }))
#     print(reverse_lazy('not found'))
#
#     context = {
#         'number': random.randint(0, 1024),
#         'numbers': [random.randint(0, 1024) for _ in range(16)],
#     }
#     return render(request, 'index.html', context, content_type='text/html')
#
#
# def not_found(request):
#     # return HttpResponseNotFound()
#     raise Http404
#
#
# def go_to_home(request):
#     return redirect('index',)
#
#
# def department_details(request, dep_id):
#     return HttpResponse(f'This is department {dep_id}')
#
#
# def list_departments(request):
#     department = Department(
#         name=f'Department {random.randint(1, 1024)}',
#     )
#     department.save()
#     Department.objects.create(
#         name=f'Department {random.randint(1, 1024)}',
#     )
#
#     print(list(Department.objects.filter(name='TV App')))
#     print(Department.objects.get(name='TV App'))
#
#     context = {
#         'departments': Department.objects.prefetch_related('employee_set').all(),
#         'employees': Employee.objects.all()
#     }
#     return render(request, 'list_of_departments.html', context)


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             },
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=40,
#     )
#
#     egn = forms.CharField(
#         max_length=10,
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software developer'),
#             (2, 'QA Engineer'),
#             (3, 'DevOps Specialist'),
#         )
#     )
#
#     company = forms.ChoiceField(
#         choices=(
#             (Employee.SOFTUNI, Employee.SOFTUNI),
#             (Employee.GOOGLE, Employee.GOOGLE),
#             (Employee.FACEBOOK, Employee.FACEBOOK),
#         )
#     )


class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot')

    class Meta:
        model = Employee
        fields = '__all__'


class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'},
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name', 'Last name'),
        ),
    )


def home(request):
    context = {
        'employee_form': EmployeeForm(),
    }
    return render(request, 'index.html', context)


# def create_employee(request):
#     if request.method == 'GET':
#         context = {
#             'employee_form': EmployeeForm(),
#         }
#         return render(request, 'employees/create.html', context)
#     else:
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             redirect('index')
#         context = {
#             'employee_form': employee_form,
#         }
#         return render(request, 'employees/create.html', context)


def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     egn=employee_form.cleaned_data['egn'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     company=employee_form.cleaned_data['company'],
            #     department_id=1,
            # )
            # emp = Employee(
            #     **employee_form.cleaned_data,
            #     department_id=1,
            # )
            # emp.save()
            employee_form.save()
            return redirect('index')
    else:
        employee_form = EmployeeForm()

    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'employees/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee_form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }
    return render(request, 'employees/edit.html', context)

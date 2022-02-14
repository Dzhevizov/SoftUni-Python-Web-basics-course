from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django101.tasks.models import Task


# def home(request):
#     items = Task.objects.all()
#     items_strings = ''.join(f'<li>{t.title}</li>' for t in items)
#     html = f'''
#     <h1>It works!</h1>
#     <ul>
#     {items_strings}
#     </ul>
#     '''
#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'It works!',
        'tasks': Task.objects.all()
        # 'tasks': []
    }
    return render(request, 'home.html', context)

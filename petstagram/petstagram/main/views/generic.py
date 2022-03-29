from django.shortcuts import render, redirect

from petstagram.main.helpers import get_profile
from petstagram.main.models import PetsPhoto


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    if not profile:
        redirect('401')
    pet_photos = PetsPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)

from django.urls import path

from my_music_app.main.views import show_home, add_album, show_album_details, edit_album, delete_album, \
    show_profile_details, delete_profile, create_profile

urlpatterns = (
    path('', show_home, name='index'),

    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', show_album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', show_profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile')
)

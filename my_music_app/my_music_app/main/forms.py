from django import forms
from django.forms import TextInput, EmailInput, NumberInput, URLInput, Textarea

from my_music_app.helpers import BootstrapFormMixin
from my_music_app.main.models import Profile, Album


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'age': NumberInput(attrs={'placeholder': 'Age'}),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': TextInput(attrs={'placeholder': 'Artist'}),
            'description': Textarea(attrs={'placeholder': 'Description'}),
            'image': URLInput(attrs={'placeholder': 'Image URL'}),
            'price': NumberInput(attrs={'placeholder': 'Price'}),
        }


class EditAlbumForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': TextInput(attrs={'placeholder': 'Artist'}),
            'description': Textarea(attrs={'placeholder': 'Description'}),
            'image': URLInput(attrs={'placeholder': 'Image URL'}),
            'price': NumberInput(attrs={'placeholder': 'Price'}),
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')

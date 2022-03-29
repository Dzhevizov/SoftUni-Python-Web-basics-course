from django.contrib import admin

from petstagram.main.models import Pet, Profile, PetsPhoto


class PetInLineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInLineAdmin,)
    list_display = ('first_name', 'last_name')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetsPhoto)
class PetsPhotoAdmin(admin.ModelAdmin):
    pass

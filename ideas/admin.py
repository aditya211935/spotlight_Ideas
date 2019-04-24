from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Idea
"""
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('bio',)}),
        ('Permissions', {'fields': ('first_name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'bio', 'location')}
        ),
    )
    #list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
"""
admin.site.register(Idea)
admin.site.register(CustomUser)

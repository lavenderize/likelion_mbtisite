from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm
from .models import MyUser

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    model = MyUser
    list_display = ['email', 'nickname', 'mbti']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nickname', 'mbti')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )
    filter_horizontal = []
    list_filter = ['is_active', 'is_admin']
    ordering = ['email']

admin.site.register(MyUser, CustomUserAdmin)

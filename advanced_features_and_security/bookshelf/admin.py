
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

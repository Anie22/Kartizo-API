from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import *
from django.utils.html import format_html


class UserAccountAdmin(BaseUserAdmin):
    list_display = ('first_name', 'last_name', 'user_name', 'date_joined', 'is_admin', 'is_active')
    search_fields = ('first_name', 'email')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter=('last_login',)
    fieldsets = ()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('first_name', 'last_name', 'user_name', 'email', 'password1', 'password2')
        }),
    )

    ordering=('first_name',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'User_photo')
    fieldsets = ()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('user_photo', 'user')
        }),
    )

    def User_photo(self, obj):
        return format_html('<img src="{}" style="max-width:90px; max-height:90px"/>'.format(obj.user_photo.url))

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(UserProfile, ProfileAdmin)
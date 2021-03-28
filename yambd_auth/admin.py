from django.contrib import admin

from yambd_auth.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email')
    search_fields = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)

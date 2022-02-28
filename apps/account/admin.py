from django.contrib import admin
from apps.account.models import MyUser
from django.contrib.auth.admin import UserAdmin


# UserAdmin.


class MyUserAdmin(UserAdmin):
    model = MyUser
    fieldsets = (
        ('اطلاعات کاربری', {
            'fields': (
                'phone', 'username', 'email', 'otp', 'otp_create_time', 'is_active', 'password'
            )}),
        ('دسترسی', {
            'fields': (
                ('is_superuser', 'is_staff', 'groups')

            )}),
    )
    readonly_fields = ['otp_create_time']
    list_display = ('phone', 'username', 'email', 'is_active')
    ordering = ['pk']


admin.site.register(MyUser, MyUserAdmin)

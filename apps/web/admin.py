from django.contrib import admin
from .models import SiteSetting, Slider, SocialMedia, Footer


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'logo',)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Footer, FooterAdmin)


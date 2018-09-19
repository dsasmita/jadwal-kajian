from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ustad, Province, City, Mosque, Schedule


class UstadAdmin(admin.ModelAdmin):
    readonly_fields = ['photo_image']
    fieldsets = [
        (None,              {'fields': ['name', 'photo' ,'photo_image']}),
        ('Profile',         {'fields': ['profile_excerpt', 'profile']}),
        ('Social Media',    {'fields': ['link_youtube', 'link_fb', 'link_instagram', 'link_twitter']}),
    ]
    list_display = ['photo_image', 'name', 'profile_excerpt']
    search_fields = ['name']
    def photo_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.photo.url,
                width=100,
                height=100,
            )
        )

class MosqueAdmin(admin.ModelAdmin):
    readonly_fields = ['photo_image']
    fieldsets = [
        (None, {'fields': ['name', 'photo', 'photo_image']}),
        ('Maps', {'fields': ['latitude', 'longitude']}),
        ('Address', {'fields': ['city', 'postal_code', 'address']}),
    ]
    list_display = ['photo_image', 'name', 'get_city', 'get_province', 'address']

    def photo_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.photo.url,
                width=100,
                height=100,
            )
        )
    photo_image.short_description = 'Photo'

    def get_city(self, obj):
        return obj.city.name
    get_city.admin_order_field = 'name'
    get_city.short_description = 'City Name'

    def get_province(self, obj):
        return obj.city.province.name
    get_province.admin_order_field = 'name'
    get_province.short_description = 'Province Name'

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_province']

    def get_province(self, obj):
        return obj.province.name
    get_province.admin_order_field = 'name'
    get_province.short_description = 'Province Name'

class ScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ['photo_image']
    fieldsets = [
        (None,          {'fields': ['title', 'photo', 'photo_image']}),
        ('Info',        {'fields': ['ustad', 'excerpt', 'tags', 'description']}),
        ('Detail Info', {'fields': ['city', 'mosque', 'contact','start_from', 'end_to']}),
    ]
    list_display = ['photo_image', 'start_from', 'title', 'city', 'mosque', 'excerpt']

    def photo_image(self, obj):
        try:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.photo.url,
                    width=100,
                    height=100,
                )
            )
        except:
            return ''
    photo_image.short_description = 'Flyer'


admin.site.register(Ustad, UstadAdmin)
admin.site.register(Province)
admin.site.register(City, CityAdmin)
admin.site.register(Mosque, MosqueAdmin)
admin.site.register(Schedule, ScheduleAdmin)

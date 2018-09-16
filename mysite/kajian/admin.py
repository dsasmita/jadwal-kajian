from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ustad, Province, City, Mosque


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

admin.site.register(Ustad, UstadAdmin)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Mosque)

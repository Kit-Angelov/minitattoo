from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


@admin.register(Pic)
class HeroAdmin(admin.ModelAdmin):

    readonly_fields = ["image_view", ]

    def image_view (self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )

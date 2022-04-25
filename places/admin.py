from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, PlaceImage


class ImageInline(admin.TabularInline):
    model = PlaceImage
    fields = ('image', 'place_image', 'position')
    readonly_fields = ("place_image",)

    def place_image(self, obj):
        height = obj.image.height
        if height > 200:
            height = 200

        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='auto',
            height=height
            )
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)

from django.contrib import admin

from places.models import Place, PlaceImage


class ImageInline(admin.TabularInline):
    model = PlaceImage


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)

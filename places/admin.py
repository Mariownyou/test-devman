from django.contrib import admin
from django.db.models import fields
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from places.models import Place, PlaceImage


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    fields = ('image', 'place_image', 'position')
    readonly_fields = ("place_image",)
    extra = 1

    def place_image(self, obj):
        return format_html(
            '<img src="{}" width="{}" height={}px />',
            obj.image.url,
            'auto',
            200 if obj.image.height > 200 else obj.image.height
        )


class CustomSortableAdminMixin(SortableAdminMixin):
    """ Removes sorting for Place model because we don't need it"""

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        order_field = '_reorder_'  # for django 4
        old_order_field = '_reorder'  # for django 3
        if order_field in list_display:
            index_field = list_display.index(order_field)
        if old_order_field in list_display:
            index_field = list_display.index(old_order_field)
        list_display.pop(index_field)
        return list_display


class PlaceAdmin(CustomSortableAdminMixin, admin.ModelAdmin):
    inlines = (ImageInline,)
    list_display = ('title',)


class PlaceImageAdmin(admin.ModelAdmin):
    ordering = ('place',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)

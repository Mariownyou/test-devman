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
        height = obj.image.height
        if height > 200:
            height = 200

        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='auto',
            height=height
            )
        )


class CustomSortableAdminMixin(SortableAdminMixin):
    """ Removes sorting for Place model """

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        order_field = '_reorder_'
        if order_field in list_display:
            i = list_display.index(order_field)
            list_display.pop(i)
        return list_display


class PlaceAdmin(CustomSortableAdminMixin, admin.ModelAdmin):
    inlines = (ImageInline,)
    list_display = ('title',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)

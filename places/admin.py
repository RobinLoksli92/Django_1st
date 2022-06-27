from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    
    readonly_fields = [
        'headshot_image'
    ]
    
    def headshot_image(self, obj):
        return format_html('<img src="{url}" width="max-width" height=200px />',
            url=obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('name', 'description_short', 'description_long', 'long', 'lat')
    inlines = [
        ImageInline
    ]

    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)


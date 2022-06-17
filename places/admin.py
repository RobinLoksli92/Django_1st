from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    
    readonly_fields = [
        'headshot_image'
    ]
    
    def headshot_image(self, obj):
        return format_html('<img src="{url}" width="max-width" height=200px />',
            url=obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('name', 'description_short', 'description_long', 'long', 'lat', 'place_id')
    inlines = [
        ImageInline
    ]

    
admin.site.register(Image)


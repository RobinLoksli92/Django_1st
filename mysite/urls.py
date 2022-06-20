from django.contrib import admin
from django.urls import path, include
from .views import show_general, show_place
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_general),
    path('places/<str:place_id>', show_place),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

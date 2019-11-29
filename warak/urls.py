from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/',include('about.urls')),
    path('gallery/', include('gallery.urls')),
    path('program/', include('program.urls')),
    path('apply/', include('apply.urls')),
    path('notice/', include('notice.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
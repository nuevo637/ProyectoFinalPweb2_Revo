from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from usuarios_app import views

urlpatterns = [
    path('', include('usuarios_app.urls')),
    path('api/', include('entrenamientos_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

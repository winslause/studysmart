from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Assuming your app's URLs are in core/urls.py
    path('i18n/', set_language, name='set_language'),  # Add set_language URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
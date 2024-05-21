from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),

    # for ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'home.views.error_404'
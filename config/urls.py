
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <-- Импортируйте settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('documents/', include('documents.urls')),
    path('appeals/', include('appeals.urls')),
    path('about/', include('about.urls')),
    path('council/', include('council.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
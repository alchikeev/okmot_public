
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('apps.main.urls')),
    path('news/', include('apps.news.urls')),
    path('documents/', include('apps.documents.urls')),
    path('appeals/', include('apps.appeals.urls')),
    path('about/', include('apps.about.urls')),
    path('council/', include('apps.council.urls')),
    path('investors/', include('apps.investors.urls')),
    path('community/', include('apps.community.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('info/', include('apps.info.urls')),
    path('search/', include('apps.search.urls')),
    path('admin/tools/', include('apps.tools.urls')),
    # ... и все остальные ваши URL-адреса, которые должны быть переведены
    prefix_default_language=True, # Это опционально, но рекомендуется.
                                 # Если True, то для LANGUAGE_CODE (в вашем случае 'ru')
                                 # префикс /ru/ будет добавлен, даже если это язык по умолчанию.
                                 # Если False, то для языка по умолчанию префикса не будет (т.е. /news/ вместо /ru/news/).
                                 # Выберите вариант, который вам больше подходит.
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
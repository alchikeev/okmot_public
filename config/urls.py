
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
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('documents/', include('documents.urls')),
    path('appeals/', include('appeals.urls')),
    path('about/', include('about.urls')),
    path('council/', include('council.urls')),
    path('investors/', include('investors.urls')),
    path('community/', include('community.urls')),
    path('gallery/', include('gallery.urls')),
    path('info/', include('info.urls')),
    path('search/', include('search.urls')),
    # ... и все остальные ваши URL-адреса, которые должны быть переведены
    prefix_default_language=True, # Это опционально, но рекомендуется.
                                 # Если True, то для LANGUAGE_CODE (в вашем случае 'ru')
                                 # префикс /ru/ будет добавлен, даже если это язык по умолчанию.
                                 # Если False, то для языка по умолчанию префикса не будет (т.е. /news/ вместо /ru/news/).
                                 # Выберите вариант, который вам больше подходит.
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Accounts Api",
        default_version="v1",
        description="this is a test api for Azimi project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="f.s.azimi.2001@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny] #میپرسد که چه کسانی میتوانند این صفحه داکیومنت را ببینند؟ 
)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),    
    

    #easy to logIn & logOut
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 

    
    #documentation -> core.settings.py -> # restframework settings
    path('swagger/output.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api-docs/', include_docs_urls(title='api sample')),


    ## path('summernote/', include('django_summernote.urls')),
    ## path('robots.txt', include('robots.urls')),
    ## path('captcha/', include('captcha.urls')),
]


# serving static and media for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

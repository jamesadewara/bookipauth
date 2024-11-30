from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Bookip API",
        default_version='v1',
        description="Bookip API documentation",
        terms_of_service="https://www.bookip.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("eccomerce/", include("eccomerce.urls")),
    path("search/", include("query.urls")),
    path('admin/', admin.site.urls),
    # Swagger endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('apitest/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('apidoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
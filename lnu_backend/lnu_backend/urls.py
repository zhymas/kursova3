from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from ms_identity_web.django.msal_views_and_urls import MsalViews
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LNU Backend",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.google.com",
        contact=openapi.Contact(email="shvachko319@gmail.com"),
        license=openapi.License(name="LNU License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
]
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ENGI API",
        default_version='v1',
        description="API",
    ),
    patterns=[
        path(r'^api/v1/', include('rest_app.urls')),
    ],
    public=False,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]
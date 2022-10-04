from django.contrib import admin
from django.urls import path, include, re_path

from rest_app.views.start_page import start_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('rest_app.urls')),
    re_path('^', start_page)
]

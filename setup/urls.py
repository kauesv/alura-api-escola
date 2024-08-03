from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "API Escola"
admin.site.site_title = "API Escola"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('v1/', include('setup.routers.v1'))
]

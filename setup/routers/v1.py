
from django.urls import path, include


urlpatterns = [
    path('escola/', include('escola.urls.v1', namespace='escola')),
]


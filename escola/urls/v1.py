from django.urls import path, include
from rest_framework import routers
from escola.views import EstudanteViewSet, CursoViewSet

app_name = 'escola'

router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet, basename='Estudantes')
router.register(r'cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
    path('', include(router.urls)),
]

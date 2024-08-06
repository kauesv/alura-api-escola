from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from core.views import index
from escola import views

admin.site.site_header = "API Escola"
admin.site.site_title = "API Escola"

router = routers.DefaultRouter()
router.register('estudantes', views.EstudanteViewSet,basename='Estudantes')
router.register('cursos', views.CursoViewSet,basename='Cursos')
router.register('matriculas', views.MatriculaViewSet,basename='Matriculas')

urlpatterns = [
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('estudantes/<int:pk>/matriculas/', views.ListaMatriculasEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', views.ListaMatriculasCurso.as_view()),
]
from django.urls import path, include
from rest_framework import routers
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasEstudante, ListaMatriculasCurso

app_name = 'escola'

router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet, basename='Estudantes')
router.register(r'cursos', CursoViewSet, basename='Cursos')
router.register(r'matriculas', MatriculaViewSet, basename='matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas', ListaMatriculasEstudante.as_view()),
    path('cursos/<int:pk>/matriculas', ListaMatriculasCurso.as_view()),
]

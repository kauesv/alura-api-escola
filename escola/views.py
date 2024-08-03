from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasEstudante(generics.ListAPIView):

    serializer_class = ListaMatriculasEstudanteSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])

class ListaMatriculasCurso(generics.ListAPIView):
    
    serializer_class = ListaMatriculasCursoSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])
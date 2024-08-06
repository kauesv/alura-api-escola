from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Estudante.objects.all()#.order_by('-criado_em')

    #https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['criado_em']
    search_fields = ['nome', 'cpf']

    # Versionamento, segundo a documentação
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Curso.objects.all().order_by('-criado_em')
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Matricula.objects.all().order_by('-criado_em')
    serializer_class = MatriculaSerializer

class ListaMatriculasEstudante(generics.ListAPIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    serializer_class = ListaMatriculasEstudanteSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])

class ListaMatriculasCurso(generics.ListAPIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    serializer_class = ListaMatriculasCursoSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])
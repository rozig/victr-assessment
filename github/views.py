from .models import Project
from rest_framework import generics, renderers
from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-stars')
    renderer_classes = [renderers.JSONRenderer]
    serializer_class = ProjectSerializer

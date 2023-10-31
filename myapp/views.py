from rest_framework.generics import ListAPIView
from .models import ProjectCard
from .serializers import ProjectCardSerializer

class ProjectCardList(ListAPIView):
    queryset = ProjectCard.objects.all()
    serializer_class = ProjectCardSerializer
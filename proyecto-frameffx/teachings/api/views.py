from rest_framework import mixins, viewsets
from .serializers import TeachingSerializer
from teachings.models import Teaching
from .pagination import paginador_teaching1

class TeachingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TeachingSerializer
    pagination_class = paginador_teaching1
    def get_queryset(self):
        return Teaching.objects.all()
    
class TeachingCRUDView(viewsets.ModelViewSet):
    serializer_class = TeachingSerializer
    queryset = Teaching.objects.all()
    
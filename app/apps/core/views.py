from rest_framework.viewsets import ModelViewSet
from .models import (
    CodeQuality,
    Site
)
from .serializers import (
    CodeQualitySerializer,
    SiteSerializer
)


class CodeQualityViewSet(ModelViewSet):
    model = CodeQuality
    serializer_class = CodeQualitySerializer
    queryset = CodeQuality.objects.all()

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related('site')
        return qs


class SiteViewSet(ModelViewSet):
    model = Site
    serializer_class = SiteSerializer
    queryset = Site.objects.all()

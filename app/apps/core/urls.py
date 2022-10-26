from django.urls import path, include
from .views import (
    CodeQualityViewSet,
    SiteViewSet
)
from rest_framework_nested  import routers


router = routers.DefaultRouter()
router.register(r'CodeQualitys', CodeQualityViewSet)
site_router = routers.NestedSimpleRouter(router, r"CodeQualitys", lookup="CodeQuality")
site_router.register(r'sites', SiteViewSet)

app_name = 'api'

urlpatterns  = [
    path('', include(router.urls)),
    path('', include(site_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
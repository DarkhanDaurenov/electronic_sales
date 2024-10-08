from rest_framework.routers import DefaultRouter
from .views import NetworkElementViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'network-elements', NetworkElementViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
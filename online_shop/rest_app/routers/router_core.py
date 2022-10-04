from rest_framework import routers

from rest_app.viewsets.product import ProductViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'product', ProductViewSet, basename='product')
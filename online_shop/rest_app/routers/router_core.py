from rest_framework import routers

from rest_app.viewsets.image import ImageViewSet
from rest_app.viewsets.product import ProductViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'product', ProductViewSet, basename='product')
router.register(r'image', ImageViewSet, basename='image')

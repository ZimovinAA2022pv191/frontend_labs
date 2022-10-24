from rest_framework import routers

from rest_app.viewsets.dicts import DictProductViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'dict_product', DictProductViewSet, basename='dict_product')

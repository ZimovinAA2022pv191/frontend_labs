from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import Product
from rest_app.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', 'get', 'patch', 'delete']
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        qs = Product.objects.all()
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data, status=200)

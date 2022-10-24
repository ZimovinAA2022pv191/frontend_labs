from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.controllers.product import ProductController
from core.models import Product, DictProduct
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

    def create(self, request, **kwargs):
        name = request.data.get("name", None)
        price = request.data.get("price",None)
        description = request.data.get("description",None)
        type_product = get_object_or_404(DictProduct, pk=request.data['type_product'])
        controller = ProductController().create(name,price,description, type_product)
        serializer = ProductSerializer(controller)
        return Response(serializer.data)
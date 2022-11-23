from django.shortcuts import get_object_or_404
from drf_yasg.openapi import Parameter, IN_QUERY, FORMAT_FLOAT
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from core.controllers.product import ProductController
from core.models import Product, DictProduct
from rest_app.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', 'get', 'patch', 'delete']

    type_product = Parameter("type_product", IN_QUERY, description="id типа товара", type=FORMAT_FLOAT,
                                required=False)
    @swagger_auto_schema(
        operation_description="Список товара по типу",
        manual_parameters=[type_product],
        responses={
            200: "",
        }
    )
    def list(self, request):
        data = request.query_params
        type_product = data.get('type_product', None)

        qs = Product.objects.all()
        if type_product is not None:
            qs = qs.filter(type_product=type_product)

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
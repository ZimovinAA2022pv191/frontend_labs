from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from drf_yasg.openapi import IN_QUERY, Parameter, TYPE_INTEGER
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from core.controllers.image import ImagesController
from core.models import Image
from rest_app.serializers.image import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [FormParser, MultiPartParser]
    http_method_names = ["post", "get", "delete"]
    product_id = Parameter("product_id", IN_QUERY, description="id товара", type=TYPE_INTEGER)

    @swagger_auto_schema(
        operation_description="Получить набор сущностей для картинок",
        manual_parameters=[product_id],
        responses={
            200: ImageSerializer(many=True),
        }
    )
    def list(self, request, *args, **kwargs):
        product_id = request.query_params.get("product_id", None)
        controller = ImagesController()
        serializer = ImageSerializer(controller.get_images(product_id), many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def download(self, request, pk=None):
        image_model = get_object_or_404(Image, pk=pk)
        with image_model.path.open('rb') as image_file:
            return HttpResponse(image_file.read(), content_type="image/jpeg")

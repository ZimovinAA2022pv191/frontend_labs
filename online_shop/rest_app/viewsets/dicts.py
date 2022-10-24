from rest_framework import viewsets
from rest_framework.response import Response

from core.models import DictProduct
from rest_app.serializers.dicts import DictProductSerializer


class DictProductViewSet(viewsets.ViewSet):
    def list(self, request):
        qs = DictProduct.objects.all()
        serializer = DictProductSerializer(qs, many=True)
        return Response(serializer.data, status=200)
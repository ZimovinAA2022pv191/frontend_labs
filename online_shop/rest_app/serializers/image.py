from rest_framework import serializers

from core.models import Image


class ImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(source="path", use_url=False)
    class Meta:
        model = Image
        fields = ["id", "file", "name", "product", "date_upload"]

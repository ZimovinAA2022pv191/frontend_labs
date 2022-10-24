from rest_framework import serializers

from core.models import DictProduct


class DictSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, t):
        return t.get_type_display()

class DictProductSerializer(DictSerializer):
    class Meta:
        model = DictProduct
        fields = "__all__"

from rest_framework import serializers

from core.models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
    send_me = serializers.BooleanField(source='feedback.send_me', required=False)

    class Meta:
        model = FeedBack
        fields = ['email', 'text', 'send_me']



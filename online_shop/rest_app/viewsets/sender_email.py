from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from core.controllers.feedback import FeedBackController
from core.models import FeedBack
from rest_app.serializers.core import FeedBackSerializer


class SenderViewSet(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = FeedBackSerializer

    def create(self, request, **kwargs):
        email = request.data.get("email", None)
        text = request.data.get("text",None)
        send_me = request.data.get('send_me', None)
        controller = FeedBackController().create(email, text)
        FeedBackController(controller.pk).send_to_email(send_me)
        serializer = FeedBackSerializer(controller)
        return Response(serializer.data)



    @swagger_auto_schema(
        operation_description="Список товара по типу",
        responses={
            200: "Письмо успешно отправлено",
        }
    )
    @action(methods=["post"], detail=False)
    def send_email(self, request):
        text = request.data['textArea']
        email = request.data['email']
        send_me = request.data['send_me']
        print(text, email, send_me)
        return Response("Все ок", status=200)

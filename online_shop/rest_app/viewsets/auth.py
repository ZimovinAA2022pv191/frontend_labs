from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_app.serializers.auth import LoginSerializer


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Авторизоваться",
        request_body=LoginSerializer,
        responses={
            403: "Ошибка авторизации",
            202: "Аторизация упешна"
        }
    )
    @action(methods=["post"], detail=False)
    def login(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=202)
        return Response("Не верные данные для авторизации.", status=403)

    @swagger_auto_schema(
        operation_description="Выйти из системы",
        responses={
            401: "Вы не авторизорованы",
            400: "Ошибка выхода из системы",
            202: "Выход из системы был успешен"
        }
    )
    @action(methods=["post"], detail=False)
    def logout(self, request):
        user = request.user
        if user.is_authenticated:
            logout(request)
            return Response(status=202)
        return Response(status=404)

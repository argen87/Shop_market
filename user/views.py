from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from user import serializers
from user.send_mail import send_confirmation_email
from user.serializers import RegisterApiSerializer

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterApiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_confirmation_email(user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.filter(activation_code=activation_code).first()
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': "Successfully activated"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': "Link expired"}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer



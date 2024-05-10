from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import SignupSerializer, LoginSerializer


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    queryset = User.objects.all()


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        response = ser.save()
        return Response(response)

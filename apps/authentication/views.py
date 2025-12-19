from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginAPIView(APIView):
    def post(self, request):
        username, password = request.data.get('username'), request.data.get('password')
        if password and username:
            user = authenticate(request=request, username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password")
            token_obj, _ = Token.objects.get_or_create(user_id=user.pk)
        else:
            raise ValidationError("Username and password are required")
        return Response({"token": token_obj.key})


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
      user = request.user
      Token.objects.filter(user_id=user.pk).delete()
      return Response({"message": "Successfully logged out"})
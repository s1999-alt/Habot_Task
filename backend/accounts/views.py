from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .serializers import RegisterSerializer



class RegisterAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(
        {"message": "User registered successfully"},
        status=status.HTTP_201_CREATED
      )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)
    if not user:
      return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    refresh = RefreshToken.for_user(user)
    return Response({
      "access": str(refresh.access_token),
      "refresh": str(refresh)
    })

  





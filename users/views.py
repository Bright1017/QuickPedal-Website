from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import (
    UserRegisterSerializer,
    VerifyCodeSerializer,
    ResendCodeSerializer,
    UserProfileSerializer
)

# Register new user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


# Verify code sent to email
class VerifyCodeView(generics.GenericAPIView):
    serializer_class = VerifyCodeSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"detail": "✅ Verification successful. You can now log in."}, status=status.HTTP_200_OK)


# Resend verification code
class ResendVerificationCodeView(generics.GenericAPIView):
    serializer_class = ResendCodeSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"detail": "📩 A new verification code has been sent to your email."}, status=status.HTTP_200_OK)


# User profile view
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

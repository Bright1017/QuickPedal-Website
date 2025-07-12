from django.urls import path
from .views import (
    RegisterView,
    VerifyCodeView,
    ResendVerificationCodeView,
    UserProfileView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('verify/', VerifyCodeView.as_view(), name='user-verify'),
    path('resend-code/', ResendVerificationCodeView.as_view(), name='resend-verification-code'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
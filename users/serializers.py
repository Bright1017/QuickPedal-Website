from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'contact_number', 'password', 'password2', 'role']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        if attrs['role'] not in dict(User.ROLE_CHOICES):
            raise serializers.ValidationError({"role": "Invalid role selected."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.generate_verification_code()

        # Send email with verification code
        send_mail(
            subject='Verify Your QuickPedal Account',
            message=f'Your verification code is: {user.verification_code}',
            from_email='no-reply@quickpedal.com',
            recipient_list=[user.email],
            fail_silently=False,
        )
        return user


class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')

        try:
            user = User.objects.get(email=email, verification_code=code)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or verification code.")

        if user.is_code_expired():
            raise serializers.ValidationError("Verification code expired. Please request a new one.")

        user.is_active = True
        user.is_verified = True
        user.verification_code = ''
        user.code_generated_at = None
        user.save()
        return attrs


class ResendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        if user.is_verified:
            raise serializers.ValidationError("This account is already verified.")

        user.generate_verification_code()
        send_mail(
            subject='Your New QuickPedal Verification Code',
            message=f'Your new verification code is: {user.verification_code}',
            from_email='no-reply@quickpedal.com',
            recipient_list=[user.email],
            fail_silently=False,
        )
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'profile_photo', 'contact_number']

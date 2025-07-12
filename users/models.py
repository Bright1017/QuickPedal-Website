from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    ROLE_CHOICES = (
        ('sender', 'Sender'),
        ('rider', 'Rider'),
        ('admin', 'Admin'),
        ('investor', 'Investor'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    code_generated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username

    def generate_verification_code(self):
        """Generates a 6-digit numeric verification code and stores the generation timestamp."""
        self.verification_code = get_random_string(length=6, allowed_chars='0123456789')
        self.code_generated_at = timezone.now()
        self.save()

    def is_code_expired(self):
        """Checks if the verification code is expired (after 10 minutes)."""
        if self.code_generated_at:
            return timezone.now() > self.code_generated_at + timedelta(minutes=10)
        return True
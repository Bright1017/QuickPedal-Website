from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)


class User(AbstractUser):
    ROLE_CHOICES = (
        ('sender', 'Sender'),
        ('rider', 'Rider'),
        ('admin', 'Admin'),
        ('investor', 'Investor'),
    )

    # 
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='sender')
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    # Verification fields
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    code_generated_at = models.DateTimeField(blank=True, null=True)

    # Make email the primary login field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # username is still stored but not required for login

    def __str__(self):
        return self.email or self.username

    # --------------------------
    # Verification Code Methods
    # --------------------------
    def generate_verification_code(self):
        """Generates a 6-digit numeric verification code and stores the generation timestamp."""
        try:
            self.verification_code = get_random_string(length=6, allowed_chars='0123456789')
            self.code_generated_at = timezone.now()
            self.save()
            logger.info(f"Verification code generated for {self.email}")
            return self.verification_code
        except Exception as e:
            logger.error(f"Error generating verification code for user {self.username}: {e}")
            return None

    def is_code_expired(self):
        """Checks if the verification code is expired (after 10 minutes)."""
        try:
            if self.code_generated_at:
                return timezone.now() > self.code_generated_at + timedelta(minutes=10)
            return True
        except Exception as e:
            logger.error(f"Error checking code expiry for user {self.username}: {e}")
            return True  # fail safe: treat as expired

    def can_request_new_code(self):
        """Prevents spamming by ensuring at least 1 minute passes before generating a new code."""
        if not self.code_generated_at:
            return True
        return timezone.now() > self.code_generated_at + timedelta(minutes=1)

    def verify_code(self, code):
        """Checks if the provided code matches and is still valid. Marks user as verified if successful."""
        if self.is_code_expired():
            logger.warning(f"Verification failed: code expired for {self.email}")
            return False
        if self.verification_code == code:
            self.is_verified = True
            self.verification_code = None  # clear after success
            self.code_generated_at = None
            self.save()
            logger.info(f"User {self.email} successfully verified")
            return True
        logger.warning(f"Verification failed: wrong code for {self.email}")
        return False

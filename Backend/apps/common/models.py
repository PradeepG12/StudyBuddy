import uuid
from datetime import datetime
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.conf import settings

from .config import storage_file_path, COMMAN_DEFAULT_NULL_BLANK_CONFIG

class ImageModel(models.Model):
     
    image = models.ImageField(upload_to=storage_file_path)

    class Meta:
        abstract = True


class CustomManager(BaseUserManager):
    
    def _create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Email must be presented")
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault("is_staff", False)
        other_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **other_fields)
    
    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        
        if other_fields.get("is_staff") is not True:
                raise ValueError("Superuser must have is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(email, password, **other_fields)


class BaseModel(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        related_name="created_%(class)s",
        **COMMAN_DEFAULT_NULL_BLANK_CONFIG,
    )
    modified_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        related_name="modified_by_%(class)s",
        **COMMAN_DEFAULT_NULL_BLANK_CONFIG,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
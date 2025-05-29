from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField

from apps.common.config import COMMAN_CHAR_MAX_LENGTH, COMMAN_DEFAULT_NULL_BLANK_CONFIG
from apps.common.models import CustomManager, BaseModel, ImageModel

class ProfilePicture(ImageModel):
    pass

    class Meta:
        default_related_name = "related_user_profile"


class User(AbstractUser, BaseModel):
    
    USERNAME_FIELD = "email"
    username = None
    REQUIRED_FIELDS = []
    
    objects = CustomManager()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=COMMAN_CHAR_MAX_LENGTH)
    phone_number = PhoneNumberField(**COMMAN_DEFAULT_NULL_BLANK_CONFIG)
    picture_picture = models.OneToOneField(ProfilePicture, on_delete=models.CASCADE, **COMMAN_DEFAULT_NULL_BLANK_CONFIG)
    first_name = models.CharField(max_length=COMMAN_CHAR_MAX_LENGTH,**COMMAN_DEFAULT_NULL_BLANK_CONFIG)
    last_name = models.CharField(max_length=COMMAN_CHAR_MAX_LENGTH,**COMMAN_DEFAULT_NULL_BLANK_CONFIG)

    class Meta:
        default_related_name = "related_user"


class UserProfile(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    college = models.CharField(max_length=COMMAN_CHAR_MAX_LENGTH, **COMMAN_DEFAULT_NULL_BLANK_CONFIG)
    interests = ArrayField(
        base_field=models.CharField(max_length=COMMAN_CHAR_MAX_LENGTH),
        **COMMAN_DEFAULT_NULL_BLANK_CONFIG,
    )

    class Meta:
        default_related_name = "related_user_profile"
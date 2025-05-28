from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

from shared.models import BaseModel

User = get_user_model()


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to='post_images', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    caption = models.CharField()

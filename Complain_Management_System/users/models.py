from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_employee = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        # ImageOps compatible mode
        if image.mode not in ("L", "RGB"):
            image = image.convert("RGB")

        imagefit = ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
        imagefit.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'

class Employee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee.username}'
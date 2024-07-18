import uuid
from django.db import models

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    unique_filename = f'{uuid.uuid4()}.{ext}'
    return f'todo_images/{unique_filename}'

class Todo(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    image_url = models.URLField(max_length=200, null=True, blank=True)  # New field to store S3 URL

    def __str__(self):
        return self.task

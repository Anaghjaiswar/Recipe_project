from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    recipe_image = models.FileField(upload_to="recipes/", max_length=250, null=True,default=None)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    content = HTMLField(default="Content not available")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    issue_type = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.issue_type}"

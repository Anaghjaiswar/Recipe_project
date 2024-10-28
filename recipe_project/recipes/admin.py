from django.contrib import admin
from .models import Recipe, ContactMessage

admin.site.register(Recipe)
admin.site.register(ContactMessage)
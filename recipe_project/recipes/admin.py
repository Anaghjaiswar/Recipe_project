from django.contrib import admin
from django import forms
from .models import Recipe, ContactMessage
from tinymce.widgets import TinyMCE

# Create a custom form for the Recipe model
class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions','recipe_image']
        widgets = {
            'instructions': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'ingredients': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'description': TinyMCE(attrs={'cols': 80, 'rows': 10}),
        }

# Create a custom admin class for the Recipe model
class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    list_display = ('title', 'user', 'created_at')
    list_filter = ('user',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(ContactMessage)

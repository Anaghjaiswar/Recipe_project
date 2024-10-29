from django import forms
from .models import Recipe
from tinymce.widgets import TinyMCE


class RecipeForm(forms.ModelForm):
    # delete_image = forms.BooleanField(required=False, label="Delete current image")
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions','recipe_image']
        widgets = {
            'description': TinyMCE(attrs={'style': 'width: 100%; height: 150px;'}),
            'ingredients': TinyMCE(attrs={'style': 'width: 100%; height: 300px;'}),
            'instructions': TinyMCE(attrs={'style': 'width: 100%; height: 300px;'}),

        }


# meta class : provides flexibility in selecting fields and configuring form behavior

from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'image', 'ingredients', 'instructions']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'instructions': forms.Textarea(attrs={'rows': 8}),
        }
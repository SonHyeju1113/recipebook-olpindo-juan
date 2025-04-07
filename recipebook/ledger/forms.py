from django.forms import ModelForm
from .models import Recipe, RecipeIngredient, RecipeImage

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "author"]

class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class RecipeImageForm(ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'
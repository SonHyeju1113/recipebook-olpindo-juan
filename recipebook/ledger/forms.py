from django.forms import ModelForm
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class RecipeImageForm(ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description',]
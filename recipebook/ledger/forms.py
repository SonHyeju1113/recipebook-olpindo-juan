from django.forms import ModelForm, modelformset_factory
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name',]

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity',]

class RecipeImageForm(ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description',]
from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
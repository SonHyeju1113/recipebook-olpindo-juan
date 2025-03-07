from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)

class IngredientAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('recipe', 'ingredient', 'quantity',)
    list_display = ('recipe', 'ingredient', 'quantity',)
    list_filter = ('recipe', 'ingredient', 'quantity',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
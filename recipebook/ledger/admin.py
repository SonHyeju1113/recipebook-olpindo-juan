from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class RecipeInline(admin.TabularInline):
    model = Recipe

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

class ProfileAdmin(admin.ModelAdmin):
    inlines = [RecipeInline,]

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline, RecipeIngredientInline,]
    search_fields = ('name', 'author',)
    list_display = ('name', 'author',)
    list_filter = ('name', 'author',)

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

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
from django.urls import path
from .views import LedgerView, RecipeView, RecipeCreate, IngredientCreate, RecipeImageCreate, RecipeUpdate
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('recipes/list/', LedgerView.as_view(), name = "ledger"),
    path('recipe/<int:pk>/', RecipeView.as_view(), name = "recipe"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('', LoginView.as_view(), name='home'),
    path('recipe/add/', RecipeCreate.as_view(), name = "create"),
    path('recipe/<int:pk>/add', RecipeImageCreate.as_view(), name = "image"),
    path('recipe/ingredient/add', IngredientCreate.as_view(), name = "ingredient")
]

app_name = "ledger"
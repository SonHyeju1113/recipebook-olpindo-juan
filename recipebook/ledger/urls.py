from django.urls import path
from .views import ledger, recipe

urlpatterns = [
    path('recipes/list/', ledger.as_view(), name = "ledger"),
    path('recipe/int:<pk>/', recipe.as_view(), name = 'recipe'),
]

app_name = "ledger"
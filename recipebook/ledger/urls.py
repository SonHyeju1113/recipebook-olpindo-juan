from django.urls import path
from .views import ledger, recipe1, recipe2

urlpatterns = [
    path('recipes/list/', ledger, name = "ledger"),
    path('recipe/1/', recipe1, name = 'recipe1'),
    path('recipe/2/', recipe2, name = 'recipe2'),
]

app_name = "ledger"
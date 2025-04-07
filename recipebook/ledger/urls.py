from django.urls import path
from .views import Ledger, Recipe
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('recipes/list/', Ledger.as_view(), name = "ledger"),
    path('recipe/<int:pk>/', Recipe.as_view(), name = "recipe"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('', LoginView.as_view(), name='home')
]

app_name = "ledger"
from django.urls import path
from .views import ledger, recipe
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('recipes/list/', ledger.as_view(), name = "ledger"),
    path('recipe/<int:pk>/', recipe.as_view(), name = "recipe"),
    path('accounts/login/', LoginView.as_view(), name='login')
]

app_name = "ledger"
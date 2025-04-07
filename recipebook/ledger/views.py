from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

class Ledger(LoginRequiredMixin, ListView):
    model = Recipe
    context_object_name = 'ledger'
    template_name = 'ledger/ledger.html'
    redirect_field_name = 'accounts/login'

class Recipe(LoginRequiredMixin, DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'accounts/login'
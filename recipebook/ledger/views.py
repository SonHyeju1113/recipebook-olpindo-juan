from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ledger(LoginRequiredMixin, ListView):
    model = Recipe
    context_object_name = 'ledger'
    template_name = 'ledger.html'
    redirect_field_name = 'accounts/login'

class recipe(LoginRequiredMixin, DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipe.html'
    redirect_field_name = 'accounts/login'
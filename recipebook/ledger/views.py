from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

# Create your views here.
class ledger(ListView):
    model = Recipe
    context_object_name = 'ledger'
    template_name = 'ledger.html'

class recipe(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipe.html'
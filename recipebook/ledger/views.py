from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm, RecipeIngredientForm, RecipeImageForm

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

    def get_context_data(self, **kwargs):
        ctx = super(Recipe, self).get_context_data(**kwargs)
        ctx['form'] = RecipeForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
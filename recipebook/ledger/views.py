from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipe, Ingredient, RecipeIngredient
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

class LedgerView(LoginRequiredMixin, ListView):
    model = Recipe
    context_object_name = 'ledger'
    template_name = 'ledger/ledger.html'
    redirect_field_name = 'accounts/login'

class RecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'accounts/login'
        
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipe_add.html'
    form_class = RecipeForm
    form_class_2 = RecipeIngredientForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['form2'] = self.form_class_2()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form2 = self.form_class_2(request.POST)

        if form.is_valid() and form2.is_valid():
            recipe = form.save()
            recipe_ingredient = form2.save(commit=False)

            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()

            return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(form=form, form2=form2))

    def get_success_url(self):
        return reverse_lazy('ledger:ledger')

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    form_class = RecipeForm

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ledger/ingredient_add.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:create')

class RecipeImageCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeImageForm
    template_name = 'ledger/image_add.html'

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={'pk': self.kwargs['pk']})
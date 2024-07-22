from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.forms import DishForm, CookCreationForm, CookUpdateForm, DishSearchForm
from core.models import Cook, Dish, DishType, Country


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_countries = Country.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_countries": num_countries,
    }

    return render(request, "core/index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all()
    paginate_by = 8
    template_name = "core/dish_list.html"


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishDetaiView(generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("core:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("core:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "core/dish_confirm_delete.html"
    success_url = reverse_lazy("core:dish-list")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "core/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "core/dish_type_detail.html"
    context_object_name = "dish_type"
    paginate_by = 5


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("core:dish-type-list")
    template_name = "core/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("core:dish-type-list")
    template_name = "core/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "core/dish_type_confirm_delete.html"
    success_url = reverse_lazy("core:dish-type-list")


class CountryListView(generic.ListView):
    model = Country
    paginate_by = 10


class CountryDetailView(generic.DetailView):
    model = Country


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("core:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("core:cook-list")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return render(request, "registration/logged_out.html")

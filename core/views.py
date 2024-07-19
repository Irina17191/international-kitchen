from django.shortcuts import render
from django.views import generic
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
    # queryset = Dish.objects.select_related("dish_types") ?
    paginate_by = 5


class DishDetaiView(generic.DetailView):
    model = Dish


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "core/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class CountryListView(generic.ListView):
    model = Country
    paginate_by = 10


class CountryDetailView(generic.DetailView):
    model = Country


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5
    # template_name = "core/cook_list.html"


class CookDetailView(generic.DetailView):
    model = Cook

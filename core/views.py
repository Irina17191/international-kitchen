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


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "core/dish_type_list.html"
    context_object_name = "dish_type_list"
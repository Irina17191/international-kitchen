from django.shortcuts import render

from core.models import Cook, Dish, DishType, Country


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dishtypes = DishType.objects.count()
    num_countries = Country.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dishtypes": num_dishtypes,
        "num_countries": num_countries,
    }

    return render(request, "core/index.html", context=context)

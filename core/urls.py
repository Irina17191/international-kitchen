from django.urls import path

from core.views import (
    index,
    DishListView,
    DishTypeListView,
    CountryListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishe-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("countries", CountryListView.as_view(), name="country-list"),

]

app_name = "core"

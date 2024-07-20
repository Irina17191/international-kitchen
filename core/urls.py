from django.urls import path

from core.views import (
    index,
    DishListView,
    DishTypeListView,
    CountryListView,
    CookListView,
    CookDetailView,
    CountryDetailView,
    DishDetaiView,
    DishTypeDetailView,
    DishCreateView,
    DishUpdateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetaiView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/<int:pk>", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("countries/", CountryListView.as_view(), name="country-list"),
    path("countries/<int:pk>/", CountryDetailView.as_view(), name="country-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]

app_name = "core"

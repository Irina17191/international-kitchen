from django.urls import path

from core.views import (
    index,
    DishListView,
    DishTypeListView,

)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishe-types/", DishTypeListView.as_view(), name="dish-type-list"),

]

app_name = "core"

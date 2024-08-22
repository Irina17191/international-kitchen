from django import forms
from django.contrib.auth.forms import UserCreationForm


from core.models import Dish, Cook


class DishForm(forms.ModelForm):
    MIN_PRICE = 5

    class Meta:
        model = Dish
        fields = (
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
            "available",
        )

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < self.MIN_PRICE:
            raise forms.ValidationError(
                f"Ensure the price is >= {DishForm.MIN_PRICE}"
            )
        return price


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "years_of_experience", "country",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("first_name", "years_of_experience", "country")

    def clean_years_of_experience(self):
        return self.cleaned_data["years_of_experience"]


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by dish name",
            }
        )
    )

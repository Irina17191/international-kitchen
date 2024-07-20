from django import forms

from core.models import Dish


class DishForm(forms.ModelForm):
    MIN_PRICE = 5
    class Meta:
        model = Dish
        fields = ("name", "description", "price", "dish_type", "cooks", "available", )

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < self.MIN_PRICE:
            raise forms.ValidationError(f"Ensure the price is >= {DishForm.MIN_PRICE}")
        return price


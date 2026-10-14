from django.contrib.auth.forms import UserCreationForm
from django import forms

from kitchen.models import Cook, Dish, DishType, Reservation


class CookCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience", )


class DishCreateForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 1})
    )
    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)


class DishTypeCreateForm(forms.ModelForm):

    class Meta:
        model = DishType
        fields = "__all__"


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)


class CookCreateForm(UserCreationForm):
    dish = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = ("username", "password1", "password2", "years_of_experience", "first_name", "last_name", "dish")


class CookUpdateForm(forms.ModelForm):
    dish = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        required=False
    )

    class Meta:
        model = Cook
        fields = (
            "username",
            "years_of_experience",
            "first_name",
            "last_name",
            "dish",
        )


class CookSearchForm(forms.Form):
    username = forms.CharField(max_length=255, required=False)


class ReservationCreateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = (
            "table",
            "date",
            "time_start",
            "time_end",
            "dishes",
        )

    
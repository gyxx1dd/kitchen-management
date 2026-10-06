from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, DishCreateForm, DishSearchForm, DishTypeCreateForm, DishTypeSearchForm, \
    CookCreateForm, CookUpdateForm, CookSearchForm, ReservationCreateForm
from kitchen.mixins import StaffRequiredMixin
from kitchen.models import DishType, Cook, Dish, Table, Reservation
from kitchen.services import if_table_available


@login_required
def index(request: HttpRequest) -> HttpResponse:
    count_dish_type = DishType.objects.count()
    count_cook = Cook.objects.count()
    count_dish = Dish.objects.count()

    context = {
        "count_dish_type": count_dish_type,
        "count_cook": count_cook,
        "count_dish": count_dish,
    }

    return render(request, "kitchen/index.html", context=context)


class RegisterView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        form = DishSearchForm(initial={"name": name})
        context["form"] = form
        return context

    def get_queryset(self):
        queryset = Dish.objects.all().prefetch_related("cooks")
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data["name"]:
                return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset

class DishCreateView(LoginRequiredMixin, StaffRequiredMixin, generic.CreateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    form_class = DishCreateForm
    template_name = "kitchen/dish_create.html"


class DishUpdateView(LoginRequiredMixin, StaffRequiredMixin, generic.UpdateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    form_class = DishCreateForm
    template_name = "kitchen/dish_create.html"


class DishDeleteView(LoginRequiredMixin, StaffRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_confirm_delete.html"


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 6
    template_name = "kitchen/dishtype_list.html"
    context_object_name = "dish_type_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        form = DishTypeSearchForm(initial={"name": name})
        context["form"] = form
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data["name"]:
                return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset



class DishTypeCreateView(LoginRequiredMixin, StaffRequiredMixin, generic.CreateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    form_class = DishTypeCreateForm
    template_name = "kitchen/dishtype_create.html"


class DishTypeUpdateView(LoginRequiredMixin, StaffRequiredMixin, generic.UpdateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    form_class = DishTypeCreateForm
    template_name = "kitchen/dishtype_create.html"


class DishTypeDeleteView(LoginRequiredMixin, StaffRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dishtype_confirm_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        form = CookSearchForm(initial={"username": username})
        context["form"] = form
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data["username"]:
                return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class CookCreateView(LoginRequiredMixin, StaffRequiredMixin, generic.CreateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_create.html"
    form_class = CookCreateForm

    def form_valid(self, form):
        res = super().form_valid(form)
        self.object.dishes.set(form.cleaned_data["dish"])
        return res

class CookUpdateView(LoginRequiredMixin, StaffRequiredMixin, generic.UpdateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_create.html"
    form_class = CookUpdateForm

    def get_initial(self):
        initial = super().get_initial()
        initial["dish"] = self.object.dishes.all()
        return initial


    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.dishes.set(form.cleaned_data["dish"])
        return response


class CookDeleteView(LoginRequiredMixin, StaffRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_confirm_delete.html"


class TableListView(LoginRequiredMixin, generic.ListView):
    model = Table
    paginate_by = 8


class TableCreateView(LoginRequiredMixin, StaffRequiredMixin, generic.CreateView):
    model = Table
    success_url = reverse_lazy("kitchen:table-list")
    fields = ("number", )

class TableUpdateView(LoginRequiredMixin, StaffRequiredMixin, generic.UpdateView):
    model = Table
    success_url = reverse_lazy("kitchen:table-list")
    fields = ("number", )


class TableDeleteView(LoginRequiredMixin, StaffRequiredMixin, generic.DeleteView):
    model = Table
    success_url = reverse_lazy("kitchen:table-list")


class ReservationListView(LoginRequiredMixin, generic.ListView):
    model = Reservation
    paginate_by = 3
    def get_queryset(self):
        return Reservation.objects.filter(user__username=self.request.user.username)

class ReservationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Reservation
    success_url = reverse_lazy("kitchen:reservation-list")
    form_class = ReservationCreateForm

    def form_valid(self, form):
        table = form.cleaned_data["table"]
        date = form.cleaned_data["date"]
        time_start = form.cleaned_data["time_start"]
        time_end = form.cleaned_data["time_end"]

        res = if_table_available(table, date, time_start, time_end)

        if res is False:
            form.add_error(None, "Pls select another time")
            return super().form_invalid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReservationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Reservation
    success_url = reverse_lazy("kitchen:reservation-list")

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ReservationForAdminListView(LoginRequiredMixin, StaffRequiredMixin, generic.ListView):
    model = Reservation
    template_name = "kitchen/reservation_for_admin_list.html"
    context_object_name = "reservation_list"


class ReservationDeleteForAdminDeleteView(LoginRequiredMixin, StaffRequiredMixin, generic.DeleteView):
    model = Reservation
    context_object_name = "reservation_delete_for_admin"
    template_name = "kitchen/reservation_delete_for_admin.html"
    success_url = reverse_lazy("kitchen:reservation-admin-list")
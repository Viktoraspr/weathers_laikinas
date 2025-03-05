from django.shortcuts import render, get_object_or_404, redirect

from .helper_functions.weathers import get_temperature
from .models import City, CityWeathers
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import NameForm


def index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request=request, template_name="weathers/cities.html", context=context)


def detail(request, pk):
    city = None
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        pass

    context = {
        'city': city,
        'value': str(pk) * 5,
        'cities': City.objects.all(),
        'temperature': get_temperature(10, 10),
    }

    city_weathers = CityWeathers.objects.create(city=city, temperature=15)
    city_weathers.save()

    return render(request=request, template_name="weathers/city.html", context=context)


def add_city(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            city = City.objects.create(
                name=form.cleaned_data["city"],
                country=form.cleaned_data["country"],
                coordination_x=form.cleaned_data["coordination_x"],
                coordination_y=form.cleaned_data["coordination_y"],
            )
            city.save()
            return HttpResponseRedirect(reverse("weathers:cities"))
    else:
        form = NameForm()
    context = {"form": form}
    return render(request=request, template_name="weathers/city_add_1.html", context=context)


"""
def add_city(request):
    if request.method == "POST":
        city = City.objects.create(
            name=request.POST["city"],
            country=request.POST["country"],
            coordination_x=request.POST["coordination_x"],
            coordination_y=request.POST["coordination_y"],
        )
        city.save()
        return HttpResponseRedirect(reverse("weathers:cities", args=[10]))
    context = {}
    return render(request=request, template_name="weathers/city_add.html", context=context)
"""
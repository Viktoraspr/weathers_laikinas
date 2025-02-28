from django.shortcuts import render, get_object_or_404
from .models import City


def index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request=request, template_name="weathers/cities.html", context=context)


def detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    context = {'city': city}
    return render(request=request, template_name="weathers/city.html", context=context)

# cia turi atsirasi funckija "weathers", kur i frontenda turite nusiusti orus
# ir juos atvaizduoti
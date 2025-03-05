from django.urls import path

from . import views

app_name = 'weathers'

urlpatterns = [
    path("", views.index, name="cities"),
    path("<int:pk>", views.detail, name="city"),
    path("add", views.add_city, name="city_add"),
]


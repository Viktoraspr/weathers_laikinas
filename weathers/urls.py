from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.detail, name="city"),
    # sukurti nauja patha kuriam butu orai ir juos atvaziuti html faile
    path("orai/<int:pk>", views.orai, name="orai"),
]


from django.urls import path
from proovedores_app import views
urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarproo/",views.registrarproo,name="registrarproo")
]

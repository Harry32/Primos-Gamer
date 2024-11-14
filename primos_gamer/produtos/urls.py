from django.urls import path
from produtos import views

urlpatterns = [
    path("categorias/", views.list, name="list"),
    path("categorias/<int:id_categoria>/", views.detail, name="detail"),
    path("categoria/", views.create, name = "create")
]
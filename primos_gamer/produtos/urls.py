from django.urls import path
from produtos import views

urlpatterns = [
    path("categorias/", views.list, name="list"),
    path("categorias/<int:id_categoria>/", views.detail, name="detail"),
    # path("<int:id_produto>/results/", views.results, name="results"),
    # path("<int:id_produto>/vote/", views.vote, name="vote"),
]
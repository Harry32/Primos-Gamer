from django.urls import path
from produtos import views

urlpatterns = [
    path("categorias/", views.list, name="list"),
    path("categorias/<int:id_categoria>/", views.detail, name="detail"),
    path("categoria/", views.create, name="create"),
    path("categoria/<int:id_categoria>/", views.update, name="update")
    # path("<int:id_produto>/vote/", views.vote, name="vote"),
]
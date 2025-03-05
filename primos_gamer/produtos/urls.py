from django.urls import path
from produtos import views

urlpatterns = [
    path("", views.ProdutoView.as_view(), name="produto_list"),
    path("<int:id_produto>/", views.ProdutoView.as_view(), name="produto_detail"),
    path("categorias/", views.GetCategoriaView.as_view(), name="list"),
    path("categorias/<int:id_categoria>/", views.GetCategoriaView.as_view(), name="detail"),
    path("categoria/", views.CategoriaView.as_view(), name="create"),
    path("categoria/<int:id_categoria>/", views.CategoriaView.as_view(), name="update"),
    path("categoria/<int:id_categoria>/delete", views.DeleteCategoriaView.as_view(), name="delete")
]
from django.urls import path
from produtos import views

urlpatterns = [
    path("categorias/", views.GetCategoriaView.as_view(), name="list"),
    path("categorias/<int:id_categoria>/", views.GetCategoriaView.as_view(), name="detail"),
    path("categoria/", views.CategoriaView.as_view(), name="create"),
    path("categoria/<int:id_categoria>/", views.CategoriaView.as_view(), name="update"),
    path("categoria/<int:id_categoria>/delete/", views.DeleteCategoriaView.as_view(), name="delete"),

    path("tiposproduto/", views.GetTipoProdutoView.as_view(), name="list_tipo_produto"),
    path("tiposproduto/<int:id_tipoproduto>/", views.GetTipoProdutoView.as_view(), name="detail_tipo_produto"),
    path("tipoproduto/", views.TipoProdutoView.as_view(), name="create_tipo_produto"),
    path("tipoproduto/<int:id_tipoproduto>/", views.TipoProdutoView.as_view(), name="update_tipo_produto"),
    path("tipoproduto/<int:id_tipoproduto>/delete", views.DeleteTipoProdutoView.as_view(), name="delete_tipo_produto"),
    
]
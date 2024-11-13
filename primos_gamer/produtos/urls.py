from django.urls import path
from produtos import views

urlpatterns = [
    path("", views.list, name="list"),
    path("<int:id_produto>/", views.detail, name="detail"),
    # path("<int:id_produto>/results/", views.results, name="results"),
    # path("<int:id_produto>/vote/", views.vote, name="vote"),
]
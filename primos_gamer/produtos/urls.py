from django.urls import path
from produtos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_categoria>/', views.detail, name='detail')
]
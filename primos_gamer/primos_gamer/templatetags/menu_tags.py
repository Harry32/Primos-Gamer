from django.template import Library
from django.urls import reverse

register = Library()

@register.inclusion_tag("navbar.html")
def load_navbar():
    return {"load": "yes"}

@register.inclusion_tag("menu.html")
def load_menu():
    itens = [
        {
            'titulo': 'Home',
            'url': reverse('home'),
            'icone': 'ri-home-smile-line'
        },
        {
            'titulo': 'Produtos',
            'url': reverse('produto_list'),
            'icone': 'ri-shopping-basket-2-line'
        },
        {
            'titulo': 'Categorias',
            'url': reverse('list'),
            'icone': 'ri-book-shelf-line'
        }
    ]

    return {"itens_menu": itens}

@register.inclusion_tag("horizontal_menu.html")
def load_horizontal_menu():
    itens = [
        {
            'titulo': 'Home',
            'url': reverse('home'),
            'icone': 'ri-home-smile-line'
        },
        {
            'titulo': 'Produtos',
            'url': reverse('produto_list'),
            'icone': 'ri-shopping-basket-2-line'
        },
        {
            'titulo': 'Categorias',
            'url': reverse('list'),
            'icone': 'ri-book-shelf-line'
        },
        {
            'titulo': 'Carrinho',
            'url': reverse('carrinho'),
            'icone': 'ri-shopping-cart-2-line'
        }
    ]

    return {"itens_menu": itens}
from django.template import Library

register = Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.inclusion_tag("custom_scripts.html")
def custom_scripts(idSlider, idMinValor, idMaxValor, valorMin=0, valorMax=100, step=5):
    propriedades =  {
        "idSlider": idSlider,
        "idMinValor": idMinValor,
        "idMaxValor": idMaxValor,
        "valorMin": valorMin,
        "valorMax": valorMax,
        "step": step
    }

    return propriedades
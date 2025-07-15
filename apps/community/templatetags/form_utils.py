# community/templatetags/form_utils.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Добавляет CSS класс к полю формы Django.
    Использование: {{ field|add_class:"my-class" }}
    """
    return value.as_widget(attrs={'class': arg})
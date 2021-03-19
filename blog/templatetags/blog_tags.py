from django import template
from ..models import Category

register = template.Library()


@register.simple_tag()
def categories(count=None, order=None, parent=None):
    if parent is not None:
        category_list = Category.objects.filter(published=True, parent__isnull=parent)
    else:
        category_list = Category.objects.filter(published=True)
    if order is not None:
        category_list = category_list.order_by(order)
    if count is not None:
        category_list = category_list[:count]
    return category_list


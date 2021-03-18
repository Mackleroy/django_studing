from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(models.Model):
    name = models.CharField('Имя', max_length=30)
    is_auth = models.BooleanField('Авторизация', default=False)
    active = models.BooleanField('Активно', default=True)

    def __str__(self):
        return self.name


class ElementsOfMenu(MPTTModel):
    name = models.CharField('Название на латинеце', max_length=100)
    title = models.CharField('Название на русском', max_length=200)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительский элемент меню',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(Menu, related_name='Меню', on_delete=models.CASCADE)
    status = models.BooleanField('Статус', default=True)
    is_auth = models.BooleanField('Для авторизированных', default=False)
    anchor = models.CharField('Якорь', max_length=15)
    url = models.SlugField('Ссылка на внешний ресурс', max_length=100)
    active = models.BooleanField('Активно', default=True)
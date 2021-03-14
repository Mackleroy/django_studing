from django.db import models


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    mini_text = models.CharField('Подзаголовок', max_length=100)
    text = models.TextField('Текст', max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comments(models.Model):
    text = models.TextField('Комментарий', max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

















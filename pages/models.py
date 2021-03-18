from django.db import models


class Page(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    active = models.BooleanField('Активность', default=True)
    template = models.CharField('Шаблон', max_length=500, default='page/index.html')
    slug = models.SlugField('Url', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

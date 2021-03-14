from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import Category, Post


# def home(request):
#     if request.method == 'POST':
#         return HttpResponse('Hi')
#     elif request.method == 'GET':
#         return HttpResponse('Good')


class HomeView(View):
    """Home page"""
    def get(self, request):
        # category_list = Category.objects.all()
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})


class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/post_list.html', {'category': category})

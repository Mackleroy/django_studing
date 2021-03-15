from datetime import datetime

from django.shortcuts import render

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
        category_list = Category.objects.all()
        posts = Post.objects.filter(published=True, published_date__lte=datetime.now())
        return render(request, 'blog/post_list.html', {'posts': posts, 'categories': category_list})


class PostDetailView(View):
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post_detail.html', {'post': post, 'categories': category_list})


class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, 'blog/post_list.html', {'category': category})

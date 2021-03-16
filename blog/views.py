from datetime import datetime

from django.shortcuts import render

from django.views.generic.base import View

from .models import Category, Post, Tag


class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        posts = Post.objects.filter(published=True, published_date__lte=datetime.now())
        return render(request, 'blog/post_list.html', {'posts': posts, 'categories': category_list})


class PostDetailView(View):
    def get(self, request, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        # comments = Comment.objects.filter(post_id=post, moderation=True)
        return render(request, post.template, {
            'post': post,
            'categories': category_list,
            # 'comments': comments
        })


class CategoryView(View):
    """Вывод статей категории"""

    def get(self, request, slug):
        category_list = Category.objects.all()
        chosen_category = Category.objects.get(slug=slug)
        if chosen_category.level == 1:
            posts = Post.objects.filter(category=chosen_category, published=True)
            return render(request, 'blog/category_detail.html', {
                'categories': category_list,
                'posts': posts
            })
        elif chosen_category.level == 0:
            children_categories = Category.objects.filter(tree_id=chosen_category.tree_id, )
            posts = Post.objects.filter(category__in=children_categories, published=True)
            return render(request, 'blog/category_detail.html', {
                'categories': category_list,
                'posts': posts
            })


class TagView(View):
    def get(self, request, slug):
        category_list = Category.objects.all()
        tag = Tag.objects.get(slug=slug)
        posts = Post.objects.filter(tags=tag, published=True)
        return render(request, 'blog/post_list.html', {
            'categories': category_list,
            'posts': posts
        })

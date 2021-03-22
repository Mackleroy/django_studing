from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.base import View

from .models import Post
from .forms import CommentForm


class PostListView(View):
    """Вывод статей категории"""

    def get_queryset(self):
        return Post.objects.filter(published=True, published_date__lte=timezone.now())  # У мишани datetime.now()

    def get(self, request, category_slug=None, slug=None):
        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif slug is not None:
            posts = self.get_queryset().filter(tags__slug=slug, tags__published=True)
        else:
            posts = self.get_queryset()
        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'posts': posts})

        # CategoryView обработка родительских категорий
        # chosen_category = Category.objects.get(slug=category_slug)
        # if chosen_category.level == 1:
        #     posts = Post.objects.filter(category=chosen_category, published=True)
        #     return render(request, posts.first().get_category_template(), {
        #         'categories': category_list,
        #         'posts': posts
        #     })
        # elif chosen_category.level == 0:
        #     children_categories = Category.objects.filter(tree_id=chosen_category.tree_id)
        #     posts = Post.objects.filter(category__in=children_categories, published=True)
        #     return render(request, posts.first().get_category_template(), {
        #         'categories': category_list,
        #         'posts': posts
        #     })


class PostDetailView(View):
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs.get('slug'))
        form = CommentForm()
        return render(request, post.template, {
            'post': post,
            'form': form
        })

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('slug'))
            form.author = request.user
            form.save()
        return redirect(request.path)

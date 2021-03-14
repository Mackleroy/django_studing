from django.contrib import admin

from .models import Category, Tag, Post, Comments

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comments)

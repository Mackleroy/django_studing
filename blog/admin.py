from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Tag, Post, Comment


class ActionCategory(admin.ModelAdmin):
    def unpublish(self, request, queryset):
        queryset.update(published=False)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        queryset.update(published=True)

    publish.short_description = 'Опубликавать'
    publish.allowed_permissions = ('change',)

    def moderate(self, request, queryset):
        queryset.update(published=True)

    moderate.short_description = 'Провести модерацию'
    moderate.allowed_permissions = ('change',)

    def unmoderate(self, request, queryset):
        queryset.update(published=True)

    unmoderate.short_description = 'Снять с модерации'
    unmoderate.allowed_permissions = ('change',)


class PostsInline(admin.StackedInline):
    """Добавляем посты к ватегории через inlines"""
    model = Post
    extra = 1


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Category)
class CategoryAdmin(ActionCategory):
    list_display = ('id', 'name', 'slug', 'published', 'template')
    list_filter = ('published',)
    list_editable = ('published', 'template')
    mptt_level_indent = 20
    actions = ['unpublish', 'publish']
    list_display_links = ('name',)
    inlines = [PostsInline]


@admin.register(Post)
class PostAdmin(ActionCategory):
    list_display = ('title', 'created_date', 'published_date', 'category', 'viewed', 'published', 'status')
    list_filter = ('created_date', 'category', 'published', 'status')
    list_editable = ('published', 'status')
    actions = ['unpublish', 'publish']
    inlines = [CommentsInline]
    filter_horizontal = ('tags',)
    fieldsets = (
        ('Контент', {
            'fields': ('author', 'title', 'subtitle', 'slug')
        }),
        ('Контент 2', {
            'fields': ('mini_text', 'text', 'img')
        }),
        ('Даты', {
            'fields': ('edited_date', 'published_date')
        }),
        ('Завязки', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('tags', 'category')
        }),
        ('Настройки', {
            'classes': ('collapse',),
            'fields': ('template', 'published', 'status', 'sort', 'viewed')
        }),
    )


@admin.register(Tag)
class TagAdmin(ActionCategory):
    list_display = ('name', 'slug', 'published')
    list_filter = ('published',)
    list_editable = ('published',)
    actions = ['unpublish', 'publish']


@admin.register(Comment)
class CommentAdmin(ActionCategory):
    list_display = ('post', 'author', 'created_date', 'moderation')
    list_filter = ('post', 'author', 'created_date', 'moderation')
    list_editable = ('moderation',)
    actions = ['moderate', 'unmoderate']


admin.site.site_title = 'Course Django'
admin.site.site_header = 'Course Django 3'
